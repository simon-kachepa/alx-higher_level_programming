def read_file(filename=""):
    """Reads a text file and prints to std out"""
    with open(filename, encoding="UTF8") as f:
        print(f.read(), end="")
