def load_txt(file_name):
    with open(file_name, 'r') as file:
        # Read the entire content of the file into a string
        file_content = file.read()
    return file_content