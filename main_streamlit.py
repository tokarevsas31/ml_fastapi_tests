import streamlit as st
from transformers import pipeline


classifier = pipeline("sentiment-analysis")
st.title("Sentiment Analysis")
st.subheader("Enter the text you would like to analyze:")
item = st.text_input("Input text and press the 'Enter' key")
if len(item) > 0:
    result = classifier(item)
    st.write("Sentiment of Text: ", result[0]["label"])
    st.write("Score: ", result[0]["score"])
