import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class ScoreCalculator:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')
        self.vectorizer = TfidfVectorizer()
    
    def calculate_score(self, resume_text, job_desc_text):
        # Preprocess texts
        resume_doc = self.nlp(resume_text.lower())
        job_desc_doc = self.nlp(job_desc_text.lower())
        
        # Calculate TF-IDF vectors
        vectors = self.vectorizer.fit_transform([resume_text, job_desc_text])
        similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        
        # Convert similarity to 10-point scale
        score = round(similarity * 10, 1)
        return min(max(score, 0), 10)  # Ensure score is between 0 and 10