import datetime
import time

name = input("Welcome.. Please Enter your name: ")
presenthour = datetime.datetime.now().hour

if 5<= presenthour <=11:
    print("Good Moring, ",name)

elif 11<= presenthour <=17:
    print("Good Afternoon, ",name)

elif 17<= presenthour <=20:
    print("Good Evening, ",name)

else:
    print("Good Night")


print("Nameste! Welcome to Your ChatBot")
print("You can ask me Basic question, Type 'bye' to exit form bot")

#  ChatBot Memory Creation
response = {
    "hello" : "Hi , Welcome. How can i help you",
    "how are you" : "I am very. Thank you",
    "who are you" : "I am smart AI ChatBot",
    "motivate me" : "Keep Going. Every bug of your project makes you a better devloper",
    "happy" : "Great to hear that",
    "functions kya hote hai": "Block of reusable code"
}


# Method/Function to get response of ChatBot
def getResponse(userques):
    userques = userques.lower()
    for eachkey in response:
        if eachkey in userques:
            return response[eachkey]

    return "I am not able to telll you that..I am still in learning mode.."


#  Takes user input
while True:
    UserInput = input("Please ask your question: ")
    reply = getResponse(UserInput)
    print("Bot Response: ",reply)

    if "bye" in UserInput.lower():
        break