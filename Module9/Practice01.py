# WAP to open a file named certificate in read a text from file
#  Find it contai the word live

file = open("certificate.txt", "r")

dataOffile = file.read()

dataOffile = dataOffile.lower()

if "live" in dataOffile:
    print("Yes, Live word is present in file")
else:
    print("No..!!")

file.close()