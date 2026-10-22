
truth_table = {
    "inputs": ["A", "B", "C"],
    "rows": [
        ([0, 0, 0], 0),
        ([0, 0, 1], 1),
        ([0, 1, 0], 0),
        ([0, 1, 1], 1),
        ([1, 0, 0], 1),
        ([1, 0, 1], 0),
        ([1, 1, 0], 0),
        ([1, 1, 1], 1)
    ]
}

def get_canonical_sop(truth_table):
    onset_inputs = []
    for input_vals, output in truth_table["rows"]:
        if output == 1:
            onset_inputs.append(input_vals)

    for i in onset_inputs:
        print(i)

        