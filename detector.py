from keybert import KeyBERT
from duckduckgo_search import DDGS
from sentence_transformers import SentenceTransformer, util

kw_model = KeyBERT()
bert_model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_keywords(text, top_n=10):
    keywords = kw_model.extract_keywords(text, top_n=top_n)
    return [kw[0] for kw in keywords]

def search_articles(query, max_results=5):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, region='wt-wt', safesearch='moderate', max_results=max_results))
    return results

def compare_similarity(user_input, search_results):
    user_embedding = bert_model.encode(user_input, convert_to_tensor=True)
    similarities = []
    for result in search_results:
        text = result.get("body") or result.get("title") or ""
        article_embedding = bert_model.encode(text, convert_to_tensor=True)
        score = util.pytorch_cos_sim(user_embedding, article_embedding).item()
        similarities.append((score, text))
    return similarities

def generate_verdict(similarities, threshold=0.6, required_matches=3):
    match_count = sum(1 for score, _ in similarities if score >= threshold)
    verdict = "REAL" if match_count >= required_matches else "FAKE"
    return verdict, match_count
