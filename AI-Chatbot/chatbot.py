import random
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of user input and chatbot responses
pairs = [
    [r'hi|hello|hey', ['Hello!', 'Hi there!']],
    [r'what is your name?', ['I am a chatbot created for helping you.', 'You can call me ChatBot.']],
    [r'how are you?', ['I am just a computer program, but thanks for asking!', 'I am here to assist you!']],
    [r'quit', ['Bye! Take care!', 'See you later!']],
]

# Create a Chat object
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
if __name__ == '__main__':
    print("Hi, I'm a chatbot! Type 'quit' to exit.")
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit':
            print('ChatBot: Bye!')
            break
        response = chatbot.respond(user_input)
        print('ChatBot:', response if response else 'Sorry, I do not understand.')