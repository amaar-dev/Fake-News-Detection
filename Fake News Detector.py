from keybert import KeyBERT

user_input = """
NASA plans to launch a mission to explore Europa, Jupiter's icy moon, searching for signs of life.
"""


kw_model = KeyBERT()

keywords = kw_model.extract_keywords(user_input, top_n=10) #extract 10 keywords

keywords_only = [kw[0] for kw in keywords]

print("Extracted Keywords:", keywords_only)
### The code above uses KeyBERT to extract keywords from a given text input and shows the top 10 keywords in the form of a list.#

### The following will use the extracted keywords to search for news articles related to them.

from duckduckgo_search import DDGS
# Use DDGS as a context manager
def search_results(query):
    print("🔍 Searching for news articles on:", query)
    with DDGS() as ddgs:
        results = list(ddgs.text(query, region='wt-wt', safesearch='moderate', max_results=5))
    if not results:
        print("❌ No results found.")
    else:
        for i, result in enumerate(results):
            print(f"\nResult {i+1}:")
            print("Title:", result.get("title", "No title"))
            print("Description:", result.get("body", "No description"))
            print("URL:", result.get("href", "No URL"))
