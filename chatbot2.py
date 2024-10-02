import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


nltk.download('punkt')
nltk.download('stopwords')

# Define a simple chatbot function
def simple_chatbot():
    print("Chatbot: Hi! How can I assist you today?")
    # Complete chatbot code in Python

def chatbot():
    print("Hello! I'm your chatbot. How can I help you today?")

    while True:
        # Getting user input and converting it to lowercase for easier matching
        user_input = input("You: ").lower()

        # Greeting
        if "hi" in user_input or "hello" in user_input:
            print("Chatbot: Hello! How can I assist you today?")
        
        # Responding to "How are you?"
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but thanks for asking! How about you?")
        
        # Asking for the chatbot's name
        elif "what is your name" in user_input:
            print("Chatbot: I'm a chatbot created to assist you with questions.")

        # Responding to a farewell
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Asking what the chatbot can do
        elif "what can you do" in user_input:
            print("Chatbot: I can answer questions, provide information, and chat with you!")

        # Asking who created the chatbot
        elif "who created you" in user_input:
            print("Chatbot: I was created by developers to assist users like you.")

        # Telling a joke
        elif "tell me a joke" in user_input:
            print("Chatbot: Why don't programmers like nature? It has too many bugs!")

        # Asking for the time
        elif "what time is it" in user_input:
            from datetime import datetime
            now = datetime.now().strftime("%H:%M")
            print(f"Chatbot: It's currently {now}.")

        # Asking for chatbot's favorite color (just for fun)
        elif "what's your favorite color" in user_input:
            print("Chatbot: I don't see colors, but if I could, I'd probably like blue!")

        # Default response for unrecognized input
        else:
            print("Chatbot: I'm sorry, I don't understand that question.")


    
    # Predefined responses for specific questions
    responses = {
        "python": "Python is a high-level, interpreted programming language known for its readability and versatility. It's widely used for web development, data analysis, artificial intelligence, scientific computing, and more.",
        "web development": "Web development involves building and maintaining websites. It includes aspects such as web design, web content development, client-side/server-side scripting, and network security configuration.",
        "machine learning": "Machine learning is a subset of artificial intelligence that focuses on building systems that can learn from and make decisions based on data. It uses algorithms to find patterns and insights in data.",
        "what is nltk": "NLTK stands for Natural Language Toolkit. It is a powerful library in Python used for natural language processing (NLP) tasks, such as tokenization, stemming, tagging, parsing, and more.",
        "help": "Sure! You can ask me about Python, web development, machine learning, or natural language processing. What would you like to know?",
    }

    while True:
        user_input = input("You: ")
        
        # Exit condition
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Tokenize the input and remove stop words
        tokens = word_tokenize(user_input.lower())  # Convert to lowercase for matching
        filtered_tokens = [word for word in tokens if word not in stopwords.words('english')]
        
        # Check for predefined topics
        found_response = False
        for token in filtered_tokens:
            if token in responses:
                print(f"Chatbot: {responses[token]}")
                found_response = True
                break
        
        if not found_response:
            print("Chatbot: I'm sorry, I don't have information on that. Can you ask about Python, web development, or machine learning?")

        # Start the chatbot
chatbot()

        
# Run the chatbot
simple_chatbot()
