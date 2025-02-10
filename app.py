#streamlit
import streamlit as st
from recommendation.recommender import get_recommendations

st.title("Fashion Style Recommender")

style_input = st.text_input("Enter your preferred fashion style (e.g., 'old money aesthetic')")

if st.button("Get Recommendations"):
    recommendations = get_recommendations(style_input)
    for item in recommendations:
        st.image(item["image_url"], caption=item["description"])
