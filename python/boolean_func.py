from itertools import product

file_path = "../inputs/simple_boolean.txt"
boolean_function = "AB+C'"
sorted_inputs = ['A', 'B', 'C']

def read_text(file_path):
    with open(file_path, "r") as file:
        boolean_function = file.read()

    return(boolean_function)


def get_primary_inputs_from_boolean(boolean_function):
    inputs = set()
    for char in boolean_function:
        if char.isalpha():
            inputs.add(char)
    sorted_inputs = list(sorted(inputs))

    return(sorted_inputs)


def generate_truth_table_from_boolean(boolean_function, sorted_inputs):
    product_terms = boolean_function.split("+")
    
    all_combinations = list(product([0, 1], repeat=len(sorted_inputs)))
    truth_table = []
    for combo in all_combinations:
        mapped_input_vals = dict(zip(sorted_inputs, combo))

        product_term_outputs = []
        for single_term in product_terms:
            input_vals = []
            for index, char in enumerate(single_term):
                if char.isalpha():
                    if index + 1 < len(single_term) and single_term[index + 1] == "'":
                        input_vals.append(1 - mapped_input_vals[char])
                    else:
                        input_vals.append(mapped_input_vals[char])

            product_term_outputs.append(int(all(input_vals)))

        truth_table.append((combo, int(any(product_term_outputs))))

    return{"inputs": sorted_inputs, "rows": truth_table}
        
                
