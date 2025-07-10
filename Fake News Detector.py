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
        return results

from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')  # small, fast, and good

def compare_similarity(user_input, search_results_list):
    print("\n🔎 Semantic Similarity Analysis:")

    user_embedding = model.encode(user_input, convert_to_tensor=True)

    for i, result in enumerate(search_results_list):
        text = result.get("body") or result.get("title") or ""
        article_embedding = model.encode(text, convert_to_tensor=True)
        similarity_score = util.pytorch_cos_sim(user_embedding, article_embedding).item()
        print(f"\nResult {i+1} Similarity Score: {similarity_score:.4f}")
        print("Text:", text)
