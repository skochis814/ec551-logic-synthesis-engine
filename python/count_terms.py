
def report_onset_minterm_count(truth_table):
    count = 0
    for input_vales, output in truth_table["rows"]:
        if output == 1:
            count += 1
    print(f"Total number of ON-Set minterms: {count}")

def report_offset_maxterm_count(truth_table):
    count = 0
    for input_vales, output in truth_table["rows"]:
        if output == 0:
            count += 1
    print(f"Total number of OFF-Set maxterms: {count}")
