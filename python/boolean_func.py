

def read_text(file_path):
    with open(file_path, "r", encoding = "utf-8") as file:
        boolean_function = file.read()

    print(boolean_function)

read_text(inputs//simple_boolean.txt)



def generate_truth_table_from_boolean(boolean_function):

