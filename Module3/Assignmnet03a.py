# Program that take total bill amount and number of friends , Cal how much each person will pay and also preint the data type of each vairaible 


TotalBill = float(input("Enter the Total Bill: "))
Friends = int(input("Enter the number of friends: "))

IndividualBill = TotalBill / Friends

print("The total Bill is: " ,TotalBill)
print("The total No Friends is: ",Friends)

print("Per Person Bill to be paid is :" , IndividualBill)