#preprocessing text logic
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import re

nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def tokenize_and_filter(message):
    """Tokenization, lowercasing, stopwords removal, and negation handling"""
    stop_words = set(stopwords.words("english"))

    # Define a list of negation words (you can expand this list)
    negations = {"not", "no", "never", "none", "nothing", "neither", "nobody", "nowhere", "hardly", "scarcely", "barely"}

    # Tokenize the input message
    tokens = word_tokenize(message)
    lemmatized_tokens = [lemmatizer.lemmatize(word, pos=wordnet.VERB) for word in tokens]
    filtered_tokens = []
    for word in lemmatized_tokens:
        # Check if the word is a negation
        if word.lower() in negations:
            filtered_tokens.append(f"neg_{word.lower()}")
        elif word.lower() not in stop_words and word.isalnum():
            filtered_tokens.append(word.lower())

    return filtered_tokens


mental_health_terms = {
    "Sadness / Depression": {
        "synonyms": [
            "Melancholy", "Blue", "Downhearted", "Low", "Gloomy", "Depressed", "Miserable",
            "Sorrowful", "Despondent", "Heartbroken", "Down in the dumps", "Disheartened"
        ],
        "slang": [
            "Feeling down", "In the dumps", "In a funk", "Having a rough time"
        ],
        "abbreviations": [
            "Dysthymia", "MDD"  # Major Depressive Disorder
        ]
    },
    "Anxiety": {
        "synonyms": [
            "Nervousness", "Worry", "Unease", "Tension", "Apprehension", "Fear", "Restlessness",
            "Panic", "Jitters", "Edginess", "Stress", "Fretfulness"
        ],
        "slang": [
            "Freaking out", "Having a meltdown", "Feeling jittery", "On edge", "Losing it"
        ],
        "abbreviations": [
            "GAD"  # Generalized Anxiety Disorder
            "Panic attacks", "PTSD", "OCD"
        ]
    },
    "Stress": {
        "synonyms": [
            "Strain", "Pressure", "Tension", "Overload", "Burnout", "Fatigue", "Worry", "Nervous strain",
            "Distress", "Frustration", "Overwork"
        ],
        "slang": [
            "Feeling overwhelmed", "Maxed out", "In the weeds", "Running on empty", "Stressed out", "Burnt out"
        ],
        "abbreviations": [
            "CBT", "EAP"
        ]
    },
    "Mood Swings": {
        "synonyms": [
            "Emotional rollercoaster", "Fluctuating mood", "Unpredictable emotions", "Up and down", "Emotional instability"
        ],
        "slang": [
            "On a bender", "Riding the emotional waves", "Hot and cold"
        ],
        "abbreviations": [
            "BPD"  # Borderline Personality Disorder
        ]
    },
    "Anger / Irritability": {
        "synonyms": [
            "Rage", "Fury", "Wrath", "Annoyance", "Frustration", "Agitation", "Irritation", "Vexation", "Bitterness", "Resentment"
        ],
        "slang": [
            "Losing your cool", "Blowing up", "Losing it", "Going off", "Hot under the collar", "Seeing red"
        ],
        "abbreviations": [
            "IED"  # Intermittent Explosive Disorder
        ]
    },
    "Loneliness / Social Isolation": {
        "synonyms": [
            "Solitude", "Isolation", "Aloneness", "Seclusion", "Abandonment", "Alienation", "Reclusion"
        ],
        "slang": [
            "Feeling left out", "Out of the loop", "All alone", "Feeling ghosted", "In your own head"
        ],
        "abbreviations": [
            "ASD"  # Autism Spectrum Disorder
        ]
    },
    "Self-esteem / Confidence Issues": {
        "synonyms": [
            "Insecurity", "Low self-worth", "Self-doubt", "Low confidence", "Self-criticism", "Imposter syndrome"
        ],
        "slang": [
            "Feeling like a fraud", "Not feeling good enough", "Self-sabotaging"
        ],
        "abbreviations": [
            "BDD"  # Body Dysmorphic Disorder
        ]
    },
    "Addiction / Substance Use Issues": {
        "synonyms": [
            "Dependence", "Habit", "Abuse", "Compulsion", "Obsession", "Craving", "Dependency", "Withdrawal"
        ],
        "slang": [
            "Getting hooked", "Chasing the high", "On a bender", "Hitting rock bottom"
        ],
        "abbreviations": [
            "SUD"  # Substance Use Disorder
            "AA", "NA"
        ]
    },
    "Eating Disorders": {
        "synonyms": [
            "Anorexia", "Bulimia", "Binge eating", "Restriction", "Overeating", "Compulsive eating", "Purging"
        ],
        "slang": [
            "Binging and purging", "Starving yourself"
        ],
        "abbreviations": [
            "ED"  # Eating Disorder
            "BED"  # Binge Eating Disorder
            "AN"  # Anorexia Nervosa
            "BN"  # Bulimia Nervosa
        ]
    },
    "Psychosis": {
        "synonyms": [
            "Delusions", "Hallucinations", "Disorganized thinking", "Paranoia", "Schizophrenia"
        ],
        "slang": [
            "Losing touch with reality", "Losing your mind", "Seeing things", "Hearing voices"
        ],
        "abbreviations": [
            "SZ"  # Schizophrenia
            "PSY"  # Psychosis
        ]
    },
    "Suicidal Thoughts": {
        "synonyms": [
            "Despair", "Hopelessness", "Self-harm", "Suicidal ideation", "Crisis"
        ],
        "slang": [
            "Feeling like you can’t go on", "At the end of your rope", "Wanting to check out"
        ],
        "abbreviations": [
            "SI"  # Suicidal Ideation
            "SAD"  # Suicide Attempt or Death
        ]
    },
    "Attention Deficit / Hyperactivity": {
        "synonyms": [
            "Inattention", "Hyperactivity", "Impulsiveness", "Disorganization", "Fidgeting", "ADHD"
        ],
        "slang": [
            "Spaciness", "Getting distracted", "Restless energy"
        ],
        "abbreviations": [
            "ADHD"
        ]
    }
}
def convert_slang_to_token(text: str) -> str:
    """
    Replace slang terms in text with their corresponding mental health category token.
    Example: "I'm feeling down and burnt out" -> "I'm Sadness / Depression and Stress"
    """
    for category, terms in mental_health_terms.items():
        # Check slangs
        for slang in terms["slang"]:
            # Use regex to replace whole phrases or words
            pattern = r'\b' + re.escape(slang) + r'\b'
            text = re.sub(pattern, category, text, flags=re.IGNORECASE)
    return text

if __name__ == "__main__":
    example_text = "I'm feeling down and burnt out. It's like I'm on edge all the time."
    result = convert_slang_to_token(example_text)
    print("Original Text:", example_text)
    print("Converted Text:", result) # Output: I'm Sadness / Depression and Stress. It's like I'm Anxiety all the time.