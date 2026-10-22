from itertools import product
import json



# Function to parse a JSON file containing a logic circuit
# Return a dictionary of gates with key as the gate ID and value as gate type and inputs
def parse_json(file_path):
    with open(file_path, "r") as file:
        circuit = json.load(file)

    gates = {}
    for node in circuit["nodes"]:
        gate_info = {
            "type": node["type"],
            "inputs": node["inputs"]
        }
        gates[node["id"]] = gate_info
    return gates



# Returns list of gate IDs in topologically sorted order
# Parameter gates is a dictionary mapping gate IDs to their types and inputs
def sort_gates(gates):
    sorted_gates = []
    while len(sorted_gates) < len(gates):
        for gate_id in gates:
            if gate_id in sorted_gates:
                continue
            ready = True
            for input in gates[gate_id]["inputs"]:
                if input in gates and input not in sorted_gates:
                    ready = False
            if ready:
                sorted_gates.append(gate_id)
    return sorted_gates



# Return list of primary input IDs
# Parameter gates is a dictionary mapping gate IDs to their types and inputs
def get_primary_inputs(gates):
    primary_inputs = set()
    for gate_id in gates:
        for input in gates[gate_id]["inputs"]:
            if input not in gates:
                primary_inputs.add(input)
    return sorted(primary_inputs)



# Returns the truth table as dictionary containing list of sorted inputs and list of tuples
# Tuples contain the input combination and the corresponding output value
# Parameter gates is a dictionary mapping gate IDs to their types and inputs
# Parameter sorted_gates is a list of gate IDs in topologically sorted order
# Parameter sorted_primary_inputs is a list of primary input IDs
def generate_truth_table_from_graph(gates, sorted_gates, sorted_primary_inputs):

    # AI WAS USED TO EFFICIENTLY FIND ALL INPUT COMBINATIONS (specifically the product function from itertools)
    all_combinations = list(product([0, 1], repeat=len(sorted_primary_inputs)))
    last_gate_id = sorted_gates[len(sorted_gates) - 1]
    truth_table = []

    # Iterate over all input combinations to generate the truth table
    for combination in all_combinations:
        primary_input_values = dict(zip(sorted_primary_inputs, combination))
        gate_outputs = {}
        for gate_id in sorted_gates:
            input_values = []
            for input in gates[gate_id]["inputs"]:
                if input in gates:
                    input_values.append(gate_outputs[input])
                else:
                    input_values.append(primary_input_values[input])
            
            if gates[gate_id]["type"] == "AND":
                gate_outputs[gate_id] = int(all(input_values))
            elif gates[gate_id]["type"] == "OR":
                gate_outputs[gate_id] = int(any(input_values))
            elif gates[gate_id]["type"] == "NOT":
                gate_outputs[gate_id] = int(not input_values[0])
            elif gates[gate_id]["type"] == "XOR":
                gate_outputs[gate_id] = int(sum(input_values) % 2)
            elif gates[gate_id]["type"] == "NAND":
                gate_outputs[gate_id] = int(not all(input_values))
            elif gates[gate_id]["type"] == "NOR":
                gate_outputs[gate_id] = int(not any(input_values))
            elif gates[gate_id]["type"] == "XNOR":
                gate_outputs[gate_id] = int(sum(input_values) % 2 == 0)

        output_value = gate_outputs[last_gate_id]
        truth_table.append((combination, output_value))
    return {"inputs": sorted_primary_inputs, "rows": truth_table}

