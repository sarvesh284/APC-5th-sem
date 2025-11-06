from FileHandling import read_file, write_file, update_file

def merge_two_files_into_third(file1, file2, file3):
    """Read file1 and file2, then write their content into file3."""
    content1 = read_file("file1.txt")
    content2 = read_file("file2.txt")

    # Combine both contents
    combined = content1 + "\n" + content2
    return write_file(file3, combined)

def insert_file_after_10_lines(file3, file4):
    """Read file4 and insert its content into file3 after first 10 lines."""
    content3 = read_file(file3)
    content4 = read_file(file4)

    # Split lines of file3
    lines = content3.split("\n")

    # Insert file4 content after 10 lines
    if len(lines) > 10:
        updated_content = "\n".join(lines[:10]) + "\n" + content4 + "\n" + "\n".join(lines[10:])
    else:
        # If file3 has less than 10 lines, just append
        updated_content = content3 + "\n" + content4

    return write_file(file3, updated_content)


if __name__ == "__main__":
  
    print(merge_two_files_into_third("file1.txt", "file2.txt", "file3.txt"))

  
    print(insert_file_after_10_lines("file3.txt", "file4.txt"))

    # Final Output
    print("\nFinal content of file3.txt:\n")
    print(read_file("file3.txt"))
