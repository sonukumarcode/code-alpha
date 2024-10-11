import nltk
from nltk.chat.util import Chat, reflections

# Pairs is a list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot created by nltk. You can call me Chatbot!", ]
    ],
    [
        r"how are you ?",
        ["I'm doing good, how about you?", ]
    ],
    [
        r"sorry (.*)",
        ["No problem", "It's alright", ]
    ],
    [
        r"I am (.*) good",
        ["Nice to hear that", "Alright, great!", ]
    ],
    [
        r"weather",
        [ "I'm not equipped to check the weather, but I hope it's sunny wherever you are!"]
    ],
    [
        r"how to do(.*)",
        ["You can search online or ask an expert to find out how to %1."]
    ],
    [
        r"tell me a joke",
        ["Why did the math book look sad? Because it had too many problems! 📚"]
    ],
    [
        r"quit",
        ["Bye, take care!", "It was nice talking to you. See you soon!", ]
    ],
]

# Create ChatBot
def nltk_chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

# Start the bot
if __name__ == "__main__":
    nltk_chatbot()
