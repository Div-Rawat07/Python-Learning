import datetime
import time

# Greeting User
name = input("Welcome.. Please Enter your name: ")
presenthour = datetime.datetime.now().hour

if 5 <= presenthour <= 11:
    print("Good Morning,", name)

elif 11 <= presenthour <= 17:
    print("Good Afternoon,", name)

elif 17 <= presenthour <= 20:
    print("Good Evening,", name)

else:
    print("Good Night,", name)

time.sleep(1)

print("\nNamaste! Welcome to Your ChatBot")
print("You can ask me basic questions.")
print("Type 'bye' to exit.\n")


# ChatBot Memory
response = {

    "hello": "Hi! How can I help you?",
    "hi": "Hello there!",
    "how are you": "I am fine. Thanks for asking.",
    "who are you": "I am a Smart AI ChatBot.",
    "your name": "My name is PyBot.",
    "motivate me": "Keep going. Small progress every day matters.",
    "happy": "Great to hear that!",
    "sad": "Don't worry. Tough times never last.",
    "python": "Python is a very easy and powerful programming language.",
    "c++": "C++ is fast and powerful for DSA and system programming.",
    "java": "Java is widely used in enterprise applications.",
    "functions kya hote hai": "Functions are reusable blocks of code.",
    "loop kya hota hai": "Loops are used to repeat tasks.",
    "array kya hai": "Array stores multiple values in a single variable.",
    "dsa": "DSA improves problem solving and coding skills.",
    "ai": "AI means Artificial Intelligence.",
    "time": f"Current time is {datetime.datetime.now().strftime('%H:%M:%S')}",
    "date": f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}",
    "thank you": "You're welcome!",
    "thanks": "Happy to help.",
    "bye": "Goodbye! Have a nice day."
}


# Function to Get Response
def getResponse(userques):

    userques = userques.lower()

    for eachkey in response:
        if eachkey in userques:
            return response[eachkey]

    return "I am still learning. Please ask something else."


# Chat Loop
while True:

    UserInput = input("\nYou: ")

    # Exit Condition
    if "bye" in UserInput.lower():
        print("\nBot is typing...")
        time.sleep(2)
        print("Bot:", response["bye"])
        break

    # Delay Effect
    print("\nBot is typing...")
    time.sleep(2)

    # Bot Reply
    reply = getResponse(UserInput)
    print("Bot:", reply)