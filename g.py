from GoogleNews import GoogleNews

query = "news"

googlenews = GoogleNews(lang='en', region='US', period='7d', encode='utf-8')
googlenews.search(query)
search_results = googlenews.results()
print("Raw results:", search_results)

for idx, article in enumerate(search_results, 1):
    content = article.get('desc', '') or article.get('title', '')
    words = content.split()
    print(f"{idx}. {' '.join(words[:10])}")
