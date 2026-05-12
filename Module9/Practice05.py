#  Print the count of no of lines in a file(tesstfile.txt)


try:
    with open("testfile.txt" , "r") as f:
        listoflines = f.readlines()
        print("The list of lines are : " , listoflines)
        print("No of lines in files: ", len(listoflines))

except:
    print("That file does not exist..!!")