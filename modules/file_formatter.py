import os

def format_file_name(name):
    return r"" + name.replace('/', '\\') if os.name == "nt" else name