# matching/profile_matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_profile(profile_text, tender_titles):
    # Combine profile text and tender titles into one list
    documents = [profile_text] + list(tender_titles)

    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Calculate cosine similarity between the profile (first vector) and all tenders
    profile_vector = tfidf_matrix[0]  # Company profile
    tender_vectors = tfidf_matrix[1:]  # Tender titles

    similarities = cosine_similarity(profile_vector, tender_vectors)

    # Flatten the result and return as a list
    match_scores = similarities.flatten()

    return match_scores
