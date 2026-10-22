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

def report_minterm_count(truth_table):
    count = 0
    for output in truth_table["rows"]:
        if output == 1:
            print(output)

report_minterm_count(truth_table)