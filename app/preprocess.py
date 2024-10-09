import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    # Process the text with spaCy
    doc = nlp(text)

    # Extract sentences (as an example)
    sentences = [sent.text for sent in doc.sents]

    # Extract keywords (tokens that are alphabetic and not stopwords)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]

    return {"sentences": sentences, "keywords": keywords}
