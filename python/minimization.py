def minterm_converter(truth_table):
    minterms = []
    for input_vals, output in truth_table["rows"]:
        if output == 1:
            minterm = ""
            for bit in input_vals:
                minterm += str(bit)
            minterms.append(minterm)
    return minterms

def find_PIs(minterms):
    terms = minterms.copy()
    PIs = []
    merges = 1

    while merges > 0:
        merges = 0
        merged = [False] * len(terms)
        loopPI = []

        for i in range(len(terms)):
            for j in range(i + 1, len(terms)):
                compare = 0

                for k in range(len(terms[i])):
                    if terms[i][k] != terms[j][k]:
                        compare += 1

                if compare == 1:
                    PI = ""

                    for k in range(len(terms[i])):
                        if terms[i][k] == terms[j][k]:
                            PI += terms[i][k]
                        else:
                            PI += "-"

                    if PI not in loopPI:
                        loopPI.append(PI)

                    merges += 1
                    merged[i] = True
                    merged[j] = True

        for i in range(len(terms)):
            if not merged[i]:
                PIs.append(terms[i])

        terms = loopPI
    return PIs

def find_EPIs(truth_table):
    minterms = minterm_converter(truth_table)
    PIs = find_PIs(minterms)

    EPIs = []
    cover_count = [0] * len(minterms)
    pi_match = [""] * len(minterms)

    for i in range(len(minterms)):
        for PI in PIs:
            match = True

            for j in range(len(minterms[i])):
                if PI[j] != "-" and minterms[i][j] != PI[j]:
                    match = False

            if match:
                cover_count[i] += 1
                pi_match[i] = PI

    for i in range(len(minterms)):
        if cover_count[i] == 1 and pi_match[i] not in EPIs:
            EPIs.append(pi_match[i])

    return EPIs

