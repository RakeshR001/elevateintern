def chatbot():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()
        if user_input == "hello":
            print("Bot: Hi there!")
        elif user_input == "how are you?":
            print("Bot: I'm just a bunch of code, but I'm doing well!")
        elif user_input == "what is your name?":
            print("Bot: My name is Chatbot.")
        elif user_input == "what is your age?":
            print("Bot: I don't have age, I'm just a bunch of coding.")
        elif user_input == "can you answer all of my questions?":
            print("Bot: I can't answer all of your questions, i have limited set of prompts to answer.")
        elif user_input == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()