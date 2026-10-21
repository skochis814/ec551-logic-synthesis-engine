import csv
import os

def export_truth_table_to_csv(truth_table):
    with open("output.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(truth_table["inputs"] + ["Outputs"])
        for input_combos, output in truth_table["truth_table"]:
            writer.writerow(list(input_combos) + [output])