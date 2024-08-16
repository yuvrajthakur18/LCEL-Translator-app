import requests
import streamlit as st

def get_groq_response(input_text, language):
    json_body = {
        "input": {
            "language": language,
            "text": f"{input_text}"
        },
        "config": {},
        "kwargs": {}
    }
    response = requests.post("http://127.0.0.1:8000/chain/invoke", json=json_body)

    try:
        # Parse JSON response
        response_data = response.json()
        
        # Extract the relevant part of the response
        output_message = response_data.get("output", "No result field in response")  # Adjust 'output' to the actual key in your response
        return output_message

    except ValueError:
        return "Error: Invalid JSON response"

## Streamlit app
st.title("LLM Application Using LCEL")

# Dropdown for language selection
languages = ["French", "Spanish", "German", "Italian","Hindi", "Punjabi","Gujrati","Bhojpuri","English"]  # Add more languages as needed
selected_language = st.selectbox("Select the target language", languages)

input_text = st.text_input("Enter the text you want to convert")

if input_text:
    st.write(get_groq_response(input_text, selected_language))