# main.py

from FileHandling import read_file, write_file, update_file

# Write to file
print(write_file("example.txt", "Hello, this is the first line."))

# Update file
print(update_file("example.txt", "This is an appended line."))

# Read file
print("File Content:\n", read_file("example.txt"))
