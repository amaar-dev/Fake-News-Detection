import streamlit as st
from detector import extract_keywords, search_articles, compare_similarity, generate_verdict

# Streamlit UI setup
st.set_page_config(page_title="Fake News Detector", layout="centered")
st.title("📰 Fake News Detector")

# Input text box
user_input = st.text_area("Paste a news article or claim:", height=200)

# Button to trigger detection
if st.button("Check News Authenticity"):
    if not user_input.strip():
        st.warning("Please enter some text first.")
    else:
        keywords_only = extract_keywords(user_input)
        query = " ".join(keywords_only)

        with st.spinner("Searching for related articles..."):
            results = search_articles(query)

        if not results:
            st.error("No related articles found.")
        else:
            similarities = compare_similarity(user_input, results)

            st.subheader("🔍 Similarity Scores")
            for i, (score, text) in enumerate(similarities):
                st.markdown(f"**Result {i+1}:** `{score:.4f}`\n\n{text[:200]}...")

            verdict, match_count = generate_verdict(similarities)
            st.markdown("---")
            st.subheader("🧠 Verdict")

            if verdict == "REAL":
                st.success(f"✅ This news is likely REAL. ({match_count} match{'es' if match_count != 1 else ''})")
            else:
                st.error(f"⚠️ This news might be FAKE. ({match_count} match{'es' if match_count != 1 else ''})")