from datetime import datetime

print("🤖 Smart AI Assistant")
print("Type 'bye' to exit.\n")

name = input("What's your name? ")

print(f"Hello {name}! Nice to meet you.")

while True:

    user = input(f"\n{name}: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How are you?")

    elif "how are you" in user:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "your name" in user:
        print("Bot: I am Smart AI Assistant.")

    elif "time" in user:
        
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif "date" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    elif user.startswith("calculate"):
        try:
            expression = user.replace("calculate", "")
            result = eval(expression)
            print("Bot: Answer =", result)
        except:
            print("Bot: Invalid calculation.")

    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        
        