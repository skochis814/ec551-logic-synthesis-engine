
# Returns string in form F=(minterm)+(minterm)+...
def get_canonical_sop(truth_table):
    canonical_sop = []
    onset_inputs = []
    for input_vals, output in truth_table["rows"]:
        if output == 1:
            onset_inputs.append(input_vals)

    for input_vals in onset_inputs:
        minterm = []
        for i, bit in enumerate(input_vals):
            if bit == 1:
                minterm.append(truth_table["inputs"][i])
            elif bit == 0:
                minterm.append(truth_table["inputs"][i] + "'")

        canonical_sop.append("(" + "".join(minterm) + ")")
        
    sop_expression = "F=" + "+".join(canonical_sop)

    print(f"Canonical SOP: {sop_expression}")



# Returns a string in form F=(maxterm)(maxterm)....
def get_canonical_pos(truth_table):
    canonical_pos = []
    offset_inputs = []
    for input_vals, output in truth_table["rows"]:
        if output == 0:
           offset_inputs.append(input_vals)

    for input_vals in offset_inputs:
        maxterm = []
        for i, bit in enumerate(input_vals):
            if bit == 1:
                maxterm.append(truth_table["inputs"][i] + "'")
            elif bit == 0:
                maxterm.append(truth_table["inputs"][i])

        canonical_pos.append("(" + "+".join(maxterm) + ")")

    pos_expression = "F=" + "".join(canonical_pos)

    print(f"Canonical POS: {pos_expression}")



def get_inverse_canonical_sop(truth_table):
    canonical_sop = []
    onset_inputs = []
    for input_vals, output in truth_table["rows"]:
        if output == 0:
            onset_inputs.append(input_vals)

    for input_vals in onset_inputs:
        minterm = []
        for i, bit in enumerate(input_vals):
            if bit == 1:
                minterm.append(truth_table["inputs"][i])
            elif bit == 0:
                minterm.append(truth_table["inputs"][i] + "'")

        canonical_sop.append("(" + "".join(minterm) + ")")
        
    sop_expression = "F'=" + "+".join(canonical_sop)

    print(f"Inverse Canonical SOP: {sop_expression}")



def get_inverse_canonical_pos(truth_table):
    canonical_pos = []
    offset_inputs = []
    for input_vals, output in truth_table["rows"]:
        if output == 1:
           offset_inputs.append(input_vals)

    for input_vals in offset_inputs:
        maxterm = []
        for i, bit in enumerate(input_vals):
            if bit == 1:
                maxterm.append(truth_table["inputs"][i] + "'")
            elif bit == 0:
                maxterm.append(truth_table["inputs"][i])

        canonical_pos.append("(" + "+".join(maxterm) + ")")

    pos_expression = "F'=" + "".join(canonical_pos)

    print(f"Inverse Canonical POS: {pos_expression}")

