"""Module providing a function replacing one line of a file."""
from pathlib import Path


def replace_line(file_path: str, line_num: int, new_line: str) -> bool:
    """Replace file line."""
    file = Path(file_path)
    if file.is_file():
        lines = []
        with file.open('r+', encoding='utf-8') as f:
            lines = f.readlines()
        if len(lines) > line_num >= 0:
            lines[line_num] = new_line
            with file.open('w', encoding='utf-8') as f:
                f.writelines(lines)
                return True
    return False
