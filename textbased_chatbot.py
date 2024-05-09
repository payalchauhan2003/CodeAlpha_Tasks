import spacy
import random

# Load spaCy's English model
nlp = spacy.load('en_core_web_sm')

# Define intents and responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I help you with?"],
    "farewell": ["Goodbye! Have a great day!", "Bye! See you soon!"],
    "general": ["I'm here to assist you with any questions you may have. Can you be more specific?",
                "How can I help you today?"]
}


# Define a function to classify intent
def classify_intent(text):
    doc = nlp(text)
    # Simple keyword matching for intents
    if any(token.text.lower() in ["hi", "hello", "hey"] for token in doc):
        return "greeting"
    elif any(token.text.lower() in ["bye", "goodbye", "see you"] for token in doc):
        return "farewell"
    else:
        return "general"


# Define a function to get a response based on the intent
def get_response(intent):
    return random.choice(responses[intent])


# Main function for chatbot interaction
def chatbot():
    print("Chatbot: Hi! I'm your virtual assistant. How can I help you today?")
    while True:
        # Get user input
        user_input = input("You: ")

        # Classify intent
        intent = classify_intent(user_input)

        # Get response based on the intent
        response = get_response(intent)

        # Output chatbot response
        print(f"Chatbot: {response}")

        # End conversation if intent is farewell
        if intent == "farewell":
            break


# Run the chatbot
if __name__ == "__main__":
    chatbot()
