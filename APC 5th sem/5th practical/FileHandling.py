

# file=open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\sample.txt","w")
# content=file.write("hiii")
# file.seek(5)

# file=open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\sample.txt","w")
# content=file.write("world")
# print(content)

# file.seek(0)
# file=open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\sample.txt","r")
# content=file.read()

# print(content)
# file.close()




with open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\sample.txt", "w") as file:
    file.write("hiii")


with open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\sample.txt", "a") as file:
    file.write(" world")

with open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\sample.txt", "r") as file:
    content = file.read()



# 2) Read from result.txt (read) and print
file = open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\sample.txt", "r")
content = file.read()
print("Content of sample.txt:\n", content)
file.close()

# 3) Write that content to result.txt
file = open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\result.txt", "w")
file.write(content)
file.close()

# 4) Read result.txt using read()
file = open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\result.txt", "r")
print("\nresult.txt with read():")
print(file.read())
file.close()

# 5) Read result.txt using readline()
file = open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\result.txt", "r")
print("\nresult.txt with readline():")
print(file.readline())   # first line
print(file.readline())   # second line
file.close()

# 6) Read result.txt using readlines()
file = open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\result.txt", "r")
print("\nresult.txt with readlines():")
print(file.readlines())  # list of all lines
file.close()

# 7) Use seek() to WRITE at a specific position, then seek(0) and read all again
file = open(r"c:\Users\sarvesh mahadik\Desktop\APC 5th sem\5th practical\result.txt", "r+")
print("\nPointer at start (tell):", file.tell())
file.seek(7)
file.write("ORANGE") 

print("Pointer after write (tell):", file.tell())
file.seek(0)                 # back to start

print("\nresult.txt AFTER seek+write, full content:")
print(file.read())           # read entire file again
file.close()

print(content)
