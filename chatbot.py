import nltk
from nltk.chat.util import Chat, reflections
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ["I'm doing well, thank you!", "I'm fine, thanks."]),
    (r'what is your name?', ["I'm a chatbot.", "You can call me a chatbot."]),
    (r'quit', ['Bye, take care.', 'Goodbye!']),
]
chatbot = Chat(patterns, reflections)
print("Hello! I'm a chatbot. How can I help you today?")
while True:
    user_input = input("> ")
    response = chatbot.respond(user_input)
    print(response)
    if user_input.lower() == 'quit':
        break
