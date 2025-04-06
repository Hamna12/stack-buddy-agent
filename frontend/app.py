# import streamlit as st
# import requests
# import os


# # ✅ StackOverflow API Details
# STACKOVERFLOW_API_URL = "https://api.stackexchange.com/2.3/search/advanced"
# SITE = "stackoverflow"

# def fetch_stackoverflow_data(query, num_results=5):
#     """
#     Fetch data from Stack Overflow API and return formatted results.
#     """
#     params = {
#         'order': 'desc',
#         'sort': 'relevance',
#         'q': query,
#         'site': SITE,
#         'pagesize': num_results
#     }

#     response = requests.get(STACKOVERFLOW_API_URL, params=params)
    
#     if response.status_code == 200:
#         data = response.json()
#         results = []
#         for item in data.get("items", []):
#             results.append({
#                 "title": item["title"],
#                 "link": item["link"],
#                 "score": item["score"],
#                 "is_answered": item["is_answered"],
#             })
#         return sorted(results, key=lambda x: x["score"], reverse=True)  # ✅ Sort by highest score
#     return []

# # ✅ Streamlit UI
# st.set_page_config(page_title="Stack Buddy Agent 🚀", layout="centered")

# st.markdown(
#     """
#     <style>
#         body {
#             background-color: #121212;
#             color: white;
#         }
#         .stTextInput>div>div>input {
#             background-color: #333;
#             color: white;
#         }
#         .stButton>button {
#             background-color: #14a76c;
#             color: white;
#             border-radius: 8px;
#             font-size: 16px;
#             font-weight: bold;
#         }
#         .stButton>button:hover {
#             background-color: #1c998b;
#         }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("🤖 Stack Buddy Agent")
# st.write("🚀 **Get the best StackOverflow solutions!**")

# query = st.text_input("🔍 **Type your question here:**", "")

# if st.button("🔎 Get Solution"):
#     if query.strip() == "":
#         st.warning("⚠️ **Please enter a valid question.**")
#     else:
#         with st.spinner("🔄 Fetching StackOverflow answers..."):
#             results = fetch_stackoverflow_data(query, num_results=5)

#         if not results:
#             st.error("❌ **No relevant answers found.**")
#         else:
#             st.success("✅ **Best Answer Found!**")

#             st.markdown("### 🔗 **Related StackOverflow Discussions:**")
#             for item in results:
#                 status = "✅ Answered" if item["is_answered"] else "❌ Unanswered"
#                 st.markdown(f"🔹 [{item['title']}]({item['link']}) - **{status}** (Score: {item['score']})")


import streamlit as st
import requests

# ✅ StackOverflow API Details
STACKOVERFLOW_API_URL = "https://api.stackexchange.com/2.3/search/advanced"
SITE = "stackoverflow"

def fetch_stackoverflow_data(query, num_results=5):
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
        return sorted(results, key=lambda x: x["score"], reverse=True)
    return []

# ✅ Streamlit Page Setup
st.set_page_config(page_title="Stack Buddy Agent 🚀", layout="centered")

# ✅ Custom Styling
st.markdown(
    """
    <style>
        html, body {
            background-color: #0F1117;
            color: #FAFAFA;
            font-family: 'Segoe UI', sans-serif;
        }
        .title {
            color: #00FFAB;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            color: #A0A0A0;
            font-size: 18px;
            text-align: center;
            margin-bottom: 40px;
        }
        .question-box input {
            background-color: #1E1E2F !important;
            color: white !important;
            border-radius: 8px;
        }
        .stButton>button {
            background-color: #00FFAB;
            color: black;
            font-weight: 600;
            padding: 0.5em 1em;
            border-radius: 6px;
            margin-top: 10px;
        }
        .result-card {
            background-color: #1E1E2F;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 15px;
        }
        .answered {
            color: #00FFAB;
            font-weight: bold;
        }
        .unanswered {
            color: #FF6B6B;
            font-weight: bold;
        }
        a {
            color: #4DA6FF;
            text-decoration: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Page Title and Description
st.markdown("<div class='title'>Stack Buddy Agent 🤖</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Ask any programming question — get the best answers from StackOverflow instantly.</div>", unsafe_allow_html=True)

# ✅ Query Input
query = st.text_input("🔍 Ask your question:", "", key="input_box")

# ✅ Button
if st.button("🔎 Get StackOverflow Results"):
    if query.strip() == "":
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Searching the StackOverflow universe..."):
            results = fetch_stackoverflow_data(query, num_results=5)

        if not results:
            st.error("No good answers found. Try a different question?")
        else:
            st.success("Here’s what we found 👇")

            for item in results:
                status = "✅ Answered" if item["is_answered"] else "❌ Unanswered"
                css_class = "answered" if item["is_answered"] else "unanswered"

                st.markdown(
                    f"""
                    <div class='result-card'>
                        <h4><a href="{item['link']}" target="_blank">{item['title']}</a></h4>
                        <p class='{css_class}'>{status}</p>
                        <p>🔺 Score: {item['score']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

# ✅ Footer CTA
st.markdown("---")
st.markdown("<center>👨‍💻 Built by Hamna & Arslan — AI Agents for Devs</center>", unsafe_allow_html=True)
