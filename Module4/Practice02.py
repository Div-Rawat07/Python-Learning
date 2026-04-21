# WAP take ur fav food name as input and print: middle of 3 char  , The last 2 char

food = input("Enter the food Item name: ")

mid = len(food)//2
op1 = food[mid-1 :mid+2]
print(op1)

op2 = food[-2:]
print(op2)


