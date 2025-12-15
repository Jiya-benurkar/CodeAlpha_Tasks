def chatbot():
    print("\n👋 Welcome to simple-rule based Chatbot!\n")
    print("The Chatbot accepts user inputs like: hello, how are you, bye")
    print("Gives reply to messages like: Hi!, I'm fine, thanks!, Goodbye!\n")

    print("🤖 Chatbot: Hello!")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hi! How may I help you?")

        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks!")

        elif user_input == "what is your name":
            print("🤖 Chatbot: I am a basic rule-based chatbot.")

        elif user_input == "help":
            print("🤖 Chatbot: You can say hello, ask how I am, ask my name, or type bye.")

        elif user_input in ["thank you", "thanks"]:
            print("🤖 Chatbot: You're welcome!")

        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")

chatbot()
