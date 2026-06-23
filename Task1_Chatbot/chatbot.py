from datetime import datetime

print("Chatbot: Hello! My name is Alexa.")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Chatbot: Hi! Nice to meet you.")

    elif user == "what is your name":
        print("Chatbot: My name is Alexa.")

    elif user == "how are you":
        print("Chatbot: I am fine, thank you!")

    elif user == "time":
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Chatbot: Current time is", current_time)

    elif user == "date":
        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Chatbot: Today's date is", current_date)

    elif user == "thanks":
        print("Chatbot: You're welcome!")

    elif user == "bye":
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")
