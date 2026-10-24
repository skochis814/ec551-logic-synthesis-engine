from itertools import combinations

def minterm_converter(truth_table):
    minterms = []
    for input_vals, output in truth_table["rows"]:
        if output == 1:
            minterm = ""
            for bit in input_vals:
                minterm += str(bit)
            minterms.append(minterm)
    return minterms

def find_PIs(truth_table):
    minterms = minterm_converter(truth_table)
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
    PIs = find_PIs(truth_table)

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

def minimize(truth_table, pos):
    if pos:
        truth_table = {
            "inputs": truth_table["inputs"],
            "rows": [(input_vals, 1-output) for input_vals, output in truth_table["rows"]]
        }

    minterms = minterm_converter(truth_table)
    PIs = find_PIs(truth_table)
    EPIs = find_EPIs(truth_table)

    minimized = EPIs.copy()
    cover_count = [0] * len(minterms)

    for i in range(len(minterms)):
        for EPI in EPIs:
            match = True

            for j in range(len(minterms[i])):
                if EPI[j] != "-" and minterms[i][j] != EPI[j]:
                    match = False

            if match:
                cover_count[i] += 1

    missing_terms = []

    for i in range(len(minterms)):
        if cover_count[i] == 0:
            missing_terms.append(minterms[i])

    remaining_PIs = []
    for PI in PIs:
        if PI not in EPIs:
            remaining_PIs.append(PI)

    if len(missing_terms) != 0:
        successful_combinations = []
        counter = 0

        for size in range(1, len(remaining_PIs) + 1):
            for comb in combinations(remaining_PIs, size):
                remaining_clone = missing_terms.copy()

                for PI in comb:
                    for minterm in missing_terms:
                        match = True

                        for j in range(len(minterm)):
                            if PI[j] != "-" and minterm[j] != PI[j]:
                                match = False

                        if match and minterm in remaining_clone:
                            remaining_clone.remove(minterm)

                if len(remaining_clone) == 0:
                    successful_combinations.append(comb)
                    counter += 1

            if counter > 0:
                break

        free_count = [0] * len(successful_combinations)

        for i in range(len(successful_combinations)):
            for minterm in successful_combinations[i]:
                for lit in minterm:
                    if lit == "-":
                        free_count[i] += 1

        minimized.extend(successful_combinations[free_count.index(max(free_count))])

    minimized_literals = 0
    for pattern in minimized:   
        for char in pattern:
            if char != "-":
                minimized_literals += 1

    literals_saved = canonical_literals - minimized_literals
    print(f"Literals saved: {literals_saved}")
    
    terms = []

    if pos:  
        for pattern in minimized:
            literals = []

            for i in range(len(pattern)):
                variable = truth_table["inputs"][i]

                if pattern[i] == "0":
                    literals.append(variable)
                elif pattern[i] == "1":
                    literals.append(variable + "'")

            if len(literals) == 0:
                return "F=0"

            terms.append("(" + "+".join(literals) + ")")

        if len(terms) == 0:
            return "F=1"

        return "F=" + "".join(terms)

    else:  
        for pattern in minimized:
            literals = []

            for i in range(len(pattern)):
                variable = truth_table["inputs"][i]

                if pattern[i] == "1":
                    literals.append(variable)
                elif pattern[i] == "0":
                    literals.append(variable + "'")

            if len(literals) == 0:
                return "F=1"

            terms.append("(" + "".join(literals) + ")")

        if len(terms) == 0:
            return "F=0"

        return "F=" + "+".join(terms)