import spacy

nlp = spacy.load("en_core_web_sm")

skills_database = [
    "python",
    "java",
    "c++",
    "sql",
    "machine learning",
    "data analysis",
    "pandas",
    "numpy",
    "tensorflow",
    "react",
    "node",
    "docker",
    "git"
]

def extract_skills(text):

    doc = nlp(text.lower())

    detected_skills = set()

    for token in doc:
        if token.text in skills_database:
            detected_skills.add(token.text)

    for chunk in doc.noun_chunks:
        if chunk.text in skills_database:
            detected_skills.add(chunk.text)

    return list(detected_skills)