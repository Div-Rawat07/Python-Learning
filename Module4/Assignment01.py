# Emoji Converter
# :) -->😊
# :( -->😞 
# D) -->😄
# ;) -->😉

str = input("Enter the one Emoji -->> :) , :( , D) , ;)  -->>  ")

str = str.replace(":)" , "😊")
str = str.replace(":(" , "😞")
str = str.replace("D)" , "😄")
str = str.replace(";)" , "😉")
print(str)
