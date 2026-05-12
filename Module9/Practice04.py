# Read only the 1 line of file 

# Create a file and write content
file = open("testfile.txt", "x")
file.write("Hello World \nWelcomee \nHiii")
file.close()

# Read only first line
with open("testfile.txt", "r") as f:
    line1 = f.readline()
    print(line1)