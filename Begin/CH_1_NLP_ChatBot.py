from textblob import TextBlob

# Define intents and their corresponding responses based on keywords
intents = {
    "hours": {
        "keywords": ["hours", "open", "close"],
        "response": "We are open from 9 AM to 5 PM, Monday to Friday."
    },
    "return":{
        "keywords" : ["refund","money back","return"],
        "response": "I'd be happy to help you with a return. Let me tranfer you to a live agent."
    }
}
def get_response(message):
    # Convert the message to lowercase for consistent keyword matching
    message = message.lower()
    # Check if the message contains any keywords associated with defined intents
    if any(word in message for word in intent_data[keywords]):
        return intent_data["response"]
    
    # Analyze the sentiment of the message using TextBlob
    sentiment = TextBlob(message).sentiment.polarity
    
    # Return a response based on the sentiment score
    return ("Thats great to hear!" if sentiment > 0 else
            "I'm sorry to hear that." if sentiment < 0 else
            "I see. Can you tell me more?")
def chat():
    # Greet the user and prompt for input
   print("ChatBot: Hello! How can I assist you today?")
   while(user_message := input("You: ").strip().lower()) not in ["exit", "quit", "bye"]:
       print(f"ChatBot: {get_response(user_message)}")
    # Continuously prompt the user for input until they choose to exit
   
    # Thank the user for chatting when they exit
   print("ChatBot: Thank you for chatting with us. Have a great day!")

if __name__ == "__main__":
    chat()  # Start the chat when the script is executed
