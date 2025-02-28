import streamlit as st
import requests

# ✅ StackOverflow API Details
STACKOVERFLOW_API_URL = "https://api.stackexchange.com/2.3/search/advanced"
SITE = "stackoverflow"

def fetch_stackoverflow_data(query, num_results=5):
    """
    Fetch data from Stack Overflow API and return formatted results.
    """
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': query,
        'site': SITE,
        'pagesize': num_results
    }

    response = requests.get(STACKOVERFLOW_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        results = []
        for item in data.get("items", []):
            results.append({
                "title": item["title"],
                "link": item["link"],
                "score": item["score"],
                "is_answered": item["is_answered"],
            })
        return sorted(results, key=lambda x: x["score"], reverse=True)  # ✅ Sort by highest score
    return []

# ✅ Streamlit UI
st.set_page_config(page_title="Stack Buddy Agent 🚀", layout="centered")

st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: #333;
            color: white;
        }
        .stButton>button {
            background-color: #14a76c;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #1c998b;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 Stack Buddy Agent")
st.write("🚀 **Get the best StackOverflow solutions!**")

query = st.text_input("🔍 **Type your question here:**", "")

if st.button("🔎 Get Solution"):
    if query.strip() == "":
        st.warning("⚠️ **Please enter a valid question.**")
    else:
        with st.spinner("🔄 Fetching StackOverflow answers..."):
            results = fetch_stackoverflow_data(query, num_results=5)

        if not results:
            st.error("❌ **No relevant answers found.**")
        else:
            st.success("✅ **Best Answer Found!**")

            st.markdown("### 🔗 **Related StackOverflow Discussions:**")
            for item in results:
                status = "✅ Answered" if item["is_answered"] else "❌ Unanswered"
                st.markdown(f"🔹 [{item['title']}]({item['link']}) - **{status}** (Score: {item['score']})")
