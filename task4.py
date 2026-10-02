print("================================")
print("       BASIC CHATBOT")
print("================================")
print("Hello! I am a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user_input = input("\nYou: ").lower()

    if user_input == "hello":
        print("Bot: Hi! How are you?")

    elif user_input == "how are you":
        print("Bot: I'm fine, thank you!")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    elif user_input == "what is your name":
        print("Bot: I am a Basic Python Chatbot.")

    elif user_input == "thank you":
        print("Bot: You're welcome!")

    else:
        print("Bot: Sorry, I don't understand that.")

print("Chatbot ended.")