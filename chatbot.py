import streamlit as st
import openai

# Define Streamlit app title
st.title("Chatbot with OpenAI")

# User input for OpenAI API key
api_key = st.text_input("Enter your OpenAI API Key:", type="password")

# Set OpenAI API key
openai.api_key = api_key

# Initialize conversation history
conversation_history = []

# Function to interact with OpenAI API
def get_chat_response(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    )
    return response['choices'][0]['message']['content']

# Handle user input and display chatbot response
if api_key:
    user_input = st.text_input("You:", "")

    if user_input:
        bot_response = get_chat_response(user_input)
        conversation_history.append({"role": "user", "content": user_input})
        conversation_history.append({"role": "assistant", "content": bot_response})
        
        st.text_area("Chatbot:", value=bot_response, height=200)
else:
    st.warning("Please enter your OpenAI API Key to start the chat.")
