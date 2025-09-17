# filehandling/fileupdate.py

def update_file(filename, content):
    """Appends new content to an existing file."""
    try:
        with open(filename, "a") as f:
            f.write("\n" + content)
        return f"Content updated successfully in {filename}"
    except FileNotFoundError:
        return f"Error: {filename} not found."
