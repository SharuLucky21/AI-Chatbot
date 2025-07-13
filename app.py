import streamlit as st
import random

# Predefined chatbot responses
responses = {
    "hello": ["Hello!", "Hi there!", "Hey! How can I help?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm fine, thanks for asking!"],
    "what is NLP": ["NLP stands for Natural Language Processing.", "It's a field of AI that helps computers understand human language."],
    "default": ["I'm not sure how to respond. Can you rephrase?"]
}

# Function to process user input
def chatbot_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])  # Return a matching response
    return random.choice(responses["default"])  # Default response

# Streamlit UI
st.title("Chatbot with NLP")

# User input
user_input = st.text_input("You:")

# When the user clicks "Send"
if st.button("Send"):
    if user_input.strip():  # Check if input is not empty
        response = chatbot_response(user_input)  # Get chatbot response
        st.write(f"🤖 Chatbot: {response}")
    else:
        st.warning("Please enter a message before sending.")
