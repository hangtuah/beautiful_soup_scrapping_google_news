import spacy

def load_spacy_model():
    """Loads the SpaCy English core model and returns the model object."""
    nlp = spacy.load('en_core_web_sm')
    return nlp

# Example usage
if __name__ == "__main__":
    nlp_model = load_spacy_model()
    print("SpaCy model loaded:", nlp_model)
