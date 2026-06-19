import streamlit as st
import requests

# ⚠️ IMPORTANT: Update this with your active Colab link!
CLOUDFLARE_API_URL = " https://core-prairie-specialized-raleigh.trycloudflare.com/v1/ask"

# UI Configuration
st.set_page_config(page_title="Socratic Tutor", page_icon="🧠")
st.title("🧠 Shourya's Socratic AI Tutor")
st.markdown("Ask me a coding or math question! I won't give you the answer, but I will guide you to it.")

# Initialize the chat memory in Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Draw the previous messages on the screen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Wait for the user to type a question
if prompt := st.chat_input("Why is my Python list out of bounds?"):
    
    # 1. Show the user's question on the screen
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Package the question for your FastAPI brain
    payload = {
        "user_id": "Shourya", 
        "query": prompt
    }
    
    # 3. Send the question over the internet (with a loading spinner!)
    with st.spinner("Thinking..."):
        try:
            response = requests.post(CLOUDFLARE_API_URL, json=payload, timeout=60)
            if response.status_code == 200:
                data = response.json()
                tutor_reply = f"*(Interaction #{data['interaction_count']})*\n\n**Hint:** {data['hint']}"
            else:
                tutor_reply = f"⚠️ Server Error: {response.text}"
        except Exception as e:
            tutor_reply = "⚠️ Could not connect to the AI Brain. Make sure your Colab cell is spinning and your link is updated!"
            
    # 4. Show the AI's hint on the screen
    with st.chat_message("assistant"):
        st.markdown(tutor_reply)
    st.session_state.messages.append({"role": "assistant", "content": tutor_reply})
