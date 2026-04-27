#  Dictionary -->> Built in data type in python use to store data in key value pair
# Key are unique
# They are mutable

dict1 = {"name":"Rahul",
        "age": 18 ,
        "city" : "Guwahati",
        "name":"Mohit"}

print(dict1) 
print(dict1["name"])
print(dict1["age"])
print(type(dict1))

dict1["city"] = "Hyderabad"

print(dict1)

dict1["subject"] = "Maths"

print(dict1)

# Removing key
dict1.pop("subject")
print(dict1)

print(dict1.keys())
print(dict1.values())
print(dict1.items())
