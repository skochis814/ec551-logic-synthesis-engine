import sys
from pathlib import Path

from python.graph_parser import parse_json, sort_gates, get_primary_inputs_from_graph, generate_truth_table_from_graph
from python.boolean_func import read_text, get_primary_inputs_from_boolean, generate_truth_table_from_boolean
from python.canonical import get_canonical_sop, get_canonical_pos, get_inverse_canonical_sop, get_inverse_canonical_pos
from python.count_terms import report_onset_minterm_count, report_offset_maxterm_count
from python.truth_table_exporter import export_truth_table_to_csv
from python.minimization import count_PIs, count_EPIs, min_SOP, min_POS
from python.verilog_gen import generate_verilog
from python.delay_estimate import estimate_delay

file_path = Path(sys.argv[1])

if file_path.suffix.lower() == ".json":
    gates = parse_json(file_path)
    sorted_gates = sort_gates(gates)
    primary_inputs = get_primary_inputs_from_graph(gates)
    truth_table = generate_truth_table_from_graph(gates, sorted_gates, primary_inputs)

elif file_path.suffix.lower() == ".txt":
    boolean_function = read_text(file_path)
    primary_inputs = get_primary_inputs_from_boolean(boolean_function)
    truth_table = generate_truth_table_from_boolean(boolean_function, primary_inputs)

get_canonical_sop(truth_table)
print("\n")
get_canonical_pos(truth_table)
print("\n")
get_inverse_canonical_sop(truth_table)
print("\n")
get_inverse_canonical_pos(truth_table)
print("\n")

report_onset_minterm_count(truth_table)
print("\n")
report_offset_maxterm_count(truth_table)

export_truth_table_to_csv(truth_table)

print("\n")
min_SOP(truth_table)
print("\n")
min_POS(truth_table)
print("\n")

print(f"Prime Implicants: {count_PIs(truth_table)}")
print(f"Essential Prime Implicants: {count_EPIs(truth_table)}")

generate_verilog(truth_table)
print("Verilog generated: generated.v")

estimate_delay(truth_table)