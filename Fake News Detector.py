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

from gnews import GNews

google_news = GNews(language='en', country='US', max_results=5)

query = " ".join(keywords_only) # join keywords to one string
print("\search query: ",query)

search_results = google_news.get_news(query) # perform search

# Display the headlines and links
for i, result in enumerate(search_results):
   if not search_results:
    print("❌ No results found from Google News.")
else:
    for i, result in enumerate(search_results):
        print(f"\nResult {i+1}:")
        print("Title:", result['title'])
        print("Description:", result['description'])
        print("URL:", result['url'])
