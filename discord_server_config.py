import os

def load_server_config(server_id, path_seperator):
    path = get_path(server_id, path_seperator)
    lines = read_file(path)
    dictionary = create_dictionary(lines, path_seperator)
    return dictionary

def get_path(server_id, path_seperator):
    path = f"{os.getcwd()}{path_seperator}Servers{path_seperator}{str(server_id)}.txt"
    if not os.path.exists(path):
        path = f"{os.getcwd()}{path_seperator}Servers{path_seperator}default_config.txt"
    return path

def read_file(path):
    lines = []
    with open(path) as file:
        lines = [line.rstrip() for line in file]
    return lines

def create_dictionary(lines, path_seperator):
    dictionary = {}
    for line in lines:
        edited_line = line.replace('|', path_seperator)
        parts = edited_line.split(':', 1)
        dictionary.update({parts[0]: parts[1]})
    return dictionary