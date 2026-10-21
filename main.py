# JSON input

file_path = "inputs\\simple_circuit.json"

from python.graph_parser import parse_json, sort_gates, get_primary_inputs, generate_truth_table

gates = parse_json(file_path)
sorted_gates = sort_gates(gates)
sorted_primary_inputs = get_primary_inputs(gates)
truth_table = generate_truth_table(gates, sorted_gates, sorted_primary_inputs)
print(truth_table)