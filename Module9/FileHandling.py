#  File Handling ->> allows python to store , read , manage data
#  saved on system - such as notes,student record , CSV files

# Type Files ->> Text Files-- Human Readable form (eg .txt,.csv.log )
            # ->>Binary Files --> Data stored in encoded form (.png, .jpg,.mp4 , pdf)



#  Opening Files -- file = open("filename","mode")

#  Files mode ->> "r" ,"w" , "a" , "x" , "t" , "b"


# Opening a file
# file = open("samplefile.txt" , "r")
# data = file.read()
# print("The data of file is :" , data)
# file.close()



#  File Reading
# Read entire file
# with open("report.txt" , "r") as f:
#     data = f.read()
#     print("File Data" , data)



#  Reading file line by line
# with open("Readfile.txt" , "r") as f:
#     line1 = f.readline()
#     line2 = f.readline()

# print("Line1:",line1)
# print("Line2:",line2)





# Automating file tasks(copy,rename,delete)

# copy files
# import shutil
# shutil.copy("demo.txt","dackup_demo.txt")



#  Rename file
# import os
# os.rename("test.txt" , "test1.txt")
# os.remove("test.txt")

