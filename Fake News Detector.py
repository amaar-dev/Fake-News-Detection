from keybert import KeyBERT

user_input = """
NASA plans to launch a mission to explore Europa, Jupiter's icy moon, searching for signs of life.
"""


kw_model = KeyBERT()

keywords = kw_model.extract_keywords(user_input, top_n=10) #extract 10 keywords

keywords_only = [kw[0] for kw in keywords]

print("Extracted Keywords:", keywords_only)
### The code above uses KeyBERT to extract keywords from a given text input and shows the top 10 keywords in the form of a list.