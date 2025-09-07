import streamlit as st
from main import get_code_review

st.title("AI Code Review Assistant")

code_input = st.text_area("Paste your Python code here:", height=300)

if st.button("Review My Code"):
    if code_input:
        with st.spinner("Reviewing your code..."):
            review_result = get_code_review(code_input)
        
        st.markdown(review_result)
    else:
        st.warning("Please paste some code to review.")
