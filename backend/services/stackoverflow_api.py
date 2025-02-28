import requests

API_URL = "https://api.stackexchange.com/2.3/search/advanced"
SITE = "stackoverflow"

def fetch_stackoverflow_data(query, num_results=5):
    """
    Fetch data from Stack Overflow API, sort by highest score, and return formatted results.
    """
    params = {
        'order': 'desc',
        'sort': 'relevance',  # ✅ Fetch relevant questions first
        'q': query,
        'site': SITE,
        'pagesize': 30  # ✅ Fetch more and filter later
    }

    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        # ✅ Extract relevant data
        results = []
        for item in data.get("items", []):
            results.append({
                "title": item["title"],
                "link": item["link"],
                "score": item["score"],  # ✅ Include StackOverflow score
                "is_answered": item["is_answered"],  # ✅ Answered status
            })
        
        # ✅ Sort by score (highest first)
        sorted_results = sorted(results, key=lambda x: x["score"], reverse=True)

        # ✅ Return only the top `num_results`
        return sorted_results[:num_results]
    
    raise Exception(f"❌ Failed to fetch data from Stack Overflow. Error: {response.status_code}")

