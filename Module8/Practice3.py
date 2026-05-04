# WAP that print the count vowel and consonent septately using function

def count(word):
    vowel = 0
    consonent = 0
    
    for i in word.lower():
        if i.isalpha():   
            if i in 'aeiou':
                vowel += 1
            else:
                consonent += 1
                
    return vowel, consonent


word = input("Enter the word: ")
vowels, consonents = count(word)

print("Vowels:", vowels)
print("Consonents:", consonents)