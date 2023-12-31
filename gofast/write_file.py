"""Module providing a function writing to file."""


def write_file(file_path, contents):
    """Write string to file."""
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(contents)
