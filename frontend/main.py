import streamlit as st
import requests

API_URL = "http://127.0.0.1:5000/news"

st.set_page_config(page_title="News Summarizer & Hindi TTS", layout="wide")

st.markdown("<h1 style='text-align: center; color: white;'>🔍 News Summarizer & Hindi TTS</h1>", unsafe_allow_html=True)

company = st.text_input("Enter Company Name", "")

if st.button("Search"):
    if company:
        with st.spinner("Fetching news..."):
            response = requests.get(API_URL, params={"company": company})
            if response.status_code == 200:
                data = response.json()
                
                st.markdown(f"## 📢 News Articles for {company}")
                for idx, article in enumerate(data["articles"]):
                    st.markdown(f"### 🔹 {article['title']}")
                    st.markdown(f"**Summary (English):** {article['summary']}")
                    st.markdown(f"**🔹 Hindi Summary:** {article['hindi_summary']}")
                    st.markdown(f"**Sentiment:** {article['sentiment']}")
                    st.markdown(f"[Read More]({article['url']})", unsafe_allow_html=True)
                    st.audio(f"http://127.0.0.1:5000{article['audio']}")
                    st.divider()

            else:
                st.error("No news found or API error.")
    else:
        st.warning("Please enter a company name!")
