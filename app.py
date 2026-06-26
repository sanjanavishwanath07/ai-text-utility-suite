import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os


load_dotenv()


api_key = os.getenv("GROQ_API_KEY")


st.set_page_config(
    page_title="AI Text Utility Suite",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 AI Text Utility Suite")
st.write("Powered by Groq LLM")


if not api_key:
    st.error("Groq API Key not found. Please check your .env file.")
    st.stop()


task = st.selectbox(
    "Choose a Utility",
    [
        "Text Summarizer",
        "Professional Email Generator",
        "Language Translator"
    ]
)


user_text = st.text_area(
    "Enter your text",
    height=250,
    placeholder="Type or paste your text here..."
)


if st.button("Generate Output"):

    if not user_text.strip():
        st.warning("Please enter some text.")
        st.stop()

    try:
        client = Groq(api_key=api_key)

        
        if task == "Text Summarizer":
            system_prompt = """
            You are a professional text summarizer.
            Summarize the given text into concise bullet points.
            Return only the summary.
            """

        elif task == "Professional Email Generator":
            system_prompt = """
            Convert the user's request into a professional business email.
            Include:
            - Subject
            - Greeting
            - Body
            - Closing
            Return only the email.
            """

        else:  
            system_prompt = """
            Translate the user's text into English.
            Return only the translated text.
            """

        with st.spinner("Generating..."):

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {
                        "role": "system",
                        "content": system_prompt
                    },
                    {
                        "role": "user",
                        "content": user_text
                    }
                ],
                temperature=0.2,
                max_tokens=1024
            )

            result = response.choices[0].message.content

        st.success("Output Generated Successfully!")

        st.subheader("Result")
        st.markdown(result)

    except Exception as e:
        st.error(f"Error: {str(e)}")
