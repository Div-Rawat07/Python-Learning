# List -->> SBuilt in data type that can store multiple value in single variable
# List are Mutable
# Srore mutiple type of DataType

myList = [10,20,30,"Rahul is a good boy",'a',]
print(myList)
print(myList[3])
print(myList[4])

myList[0] = "Mohan"
print(myList[0])


# List Slicing
print(myList[1 :4])



# List Function
marks = [10,45,32,9,8]
print(max(marks))
print(min(marks))
print(len(marks))

marks.append(34)
print(marks)

marks.insert(1,80)  # index, elemeent
print(marks)

marks.remove(8)  # Remove the 8 
print(marks)

marks.pop(2)   # Remove at index 2
print(marks)

marks.sort()
print(marks)

marks.reverse()
print(marks)



