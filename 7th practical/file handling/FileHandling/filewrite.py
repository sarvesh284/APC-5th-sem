# filehandling/filewrite.py

def write_file(filename, content):
    """Writes content to a file (overwrites if already exists)."""
    with open(filename, "w") as f:
        f.write(content)
    return f"Content written successfully to {filename}"
