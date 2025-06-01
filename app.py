import streamlit as st
from helper import preprocessing, vectorizer, get_prediction
from logger import logging

# Initialize session state
if "reviews" not in st.session_state:
    st.session_state.reviews = []
if "positive" not in st.session_state:
    st.session_state.positive = 0
if "negative" not in st.session_state:
    st.session_state.negative = 0

st.title("Sentiment Analysis")

text = st.text_area("Enter your review here:")
if st.button("Analyze"):
    logging.info(f'Text : {text}')

    preprocessed_txt = preprocessing(text).tolist()  # <-- Convert to list
    logging.info(f'Preprocessed Text : {preprocessed_txt}')

    vectorized_txt = vectorizer(preprocessed_txt)
    logging.info(f'Vectorized Text : {vectorized_txt}')

    prediction = get_prediction(vectorized_txt)
    logging.info(f'Prediction : {prediction}')

    if prediction == 'negative':
        st.session_state.negative += 1
        st.error("Prediction: Negative")
    else:
        st.session_state.positive += 1
        st.success("Prediction: Positive")

    st.session_state.reviews.insert(0, text)

# Show results
st.subheader("Summary")
st.write(f"Positive Reviews: {st.session_state.positive}")
st.write(f"Negative Reviews: {st.session_state.negative}")

st.subheader("Recent Reviews")
for review in st.session_state.reviews[:5]:
    st.write(f"• {review}")
