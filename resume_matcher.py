import json
import docx2txt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_text(file_path):
    return docx2txt.process(file_path)

def analyze_resume(file_path):
    with open('role_data.json', 'r') as f:
        role_data = json.load(f)

    resume_text = extract_text(file_path)
    roles = []
    for role, keywords in role_data.items():
        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform([resume_text, ' '.join(keywords)])
        score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
        roles.append((role, round(score * 100, 2)))

    roles.sort(key=lambda x: x[1], reverse=True)
    return roles[:3]
