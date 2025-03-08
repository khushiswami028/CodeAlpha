import nltk
from nltk.chat.util import Chat, reflection

# Download the necessary NLTK resources
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I assist you?"]
    ],
    [
        r"how are you?",
        [ "Doing well, how about you?"]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created to assist you.", "You can call me Chatbot!"]
    ],
    [
        r"quit",
        ["Goodbye! Have a great day!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.", "Can you please rephrase?"]
    ]
]

def chatbot():
    print("Hi! I'm a chatbot. Type 'quit' to exit.")
    chat = Chat(pairs, reflection)
    chat.converse()

if __name__ == "__main__":
    chatbot()