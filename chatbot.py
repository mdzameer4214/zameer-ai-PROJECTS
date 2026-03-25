class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "how are you?": "I'm just a program, but thanks for asking!",
            "help": "Sure! What do you need help with?",
            "bye": "Goodbye! Have a great day!"
        }

    def get_response(self, user_input):
        return self.responses.get(user_input.lower(), "I'm sorry, I don't understand that.")

if __name__ == "__main__":
    bot = Chatbot()
    while True:
        user_input = input("You: ")
        response = bot.get_response(user_input)
        print(f"Chatbot: {response}")
        if user_input.lower() == "bye":
            break
