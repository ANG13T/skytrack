import os

def format_file_name(name):
    if os.name == "nt": # format to windows based file path
            return r"" + name.replace('/', '\\')
    return name