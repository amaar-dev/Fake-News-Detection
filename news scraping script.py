from duckduckgo_search import DDGS

query = " "
print("🔍 Searching for news articles on:", query)

# Use DDGS as a context manager
with DDGS() as ddgs:
    results = ddgs.text(query, region='wt-wt', safesearch='moderate', max_results=5)

    for i, result in enumerate(results):
        print(f"\nResult {i+1}:")
        print("Title:", result.get("title", "No title"))
        print("Description:", result.get("body", "No description"))
        print("URL:", result.get("href", "No URL"))
# Note: Ensure you have the `duckduckgo_search` package installed.
# You can install it using pip install duckduckgo-search\[ENTER] pip install newspaper3k\[ENTER] pip install lxml_html_clean\[ENTER] pip install lxml


