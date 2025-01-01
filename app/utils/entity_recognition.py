import spacy

def download_model():
    try:
        spacy.cli.download("en_core_web_sm")
    except Exception as e:
        print(f"Error downloading SpaCy model: {e}")

download_model()

nlp1 = spacy.load("en_core_web_sm")




def general_name_entity(text):
    doc = nlp1(text)
    return {ent.text:ent.label_ for ent in doc.ents}


# Path to the external model
NER_MODEL_PATH = "external_models/psy-ner/model/model-best"
nlp2 = spacy.load(NER_MODEL_PATH)

def extract_mental_health_entities(text: str):
    """Extract entities from a given text using psy-ner."""
    doc = nlp2(text)
    return [{"entity": ent.text, "label": ent.label_} for ent in doc.ents]

if __name__ == '__main__':
    # text = "John Smith, I've been feeling low lately, just from work anxiety."
    text = """
Hi, my name is Sarah Thompson, and I've been feeling extremely anxious over the past few weeks.
I struggle to sleep at night because of overthinking about work deadlines and relationship problems.
Lately, I have also started feeling isolated, as I don't feel like socializing with friends or family.
Sometimes, I experience physical symptoms like tightness in my chest and a racing heart, especially when I think about finances or public speaking.
I’ve read about Generalized Anxiety Disorder and wonder if I might have it. Additionally, my friend recommended trying meditation or therapy, but I’m not sure where to start.
Can you provide some advice or recommend resources for dealing with pain, cough, fever, stress and anxiety? Also, does cognitive-behavioral therapy help with conditions like these?
Thank you for your help.
"""

    print( extract_mental_health_entities(text))
    print(general_name_entity(text))


#Output:
#[{'entity': 'Anxiety', 'label': 'ANXIETY DISORDERS'}, {'entity': 'anxiety', 'label': 'SYMPTOMS'}]
#{'Sarah Thompson': 'PERSON', 'the past few weeks': 'DATE', 'night': 'TIME', 'Generalized Anxiety Disorder': 'ORG'}