from transformers import pipeline

# Load Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """Analyze sentiment using a Hugging Face pretrained model."""
    result = sentiment_pipeline(text)
    return result

# Test Case for sentiment analysis
# user_message = "I'm feeling a bit overwhelmed today, but I think I'll be okay."
# sentiment = analyze_sentiment(user_message)

# print(f"Sentiment: {sentiment[0]['label']} | Confidence: {sentiment[0]['score']:.2f}")



# Load the Hugging Face emotion detection pipeline
emotion_pipeline = pipeline("text-classification",
                            model="bhadresh-savani/distilbert-base-uncased-emotion",
                            return_all_scores=True)

def analyze_emotion(text):
    """
    Analyze emotions in the given text using a pretrained DistilBERT model.
    Returns the most likely emotion and its confidence score.
    """
    results = emotion_pipeline(text)

    # Find the emotion with the highest confidence score
    top_emotion = max(results[0], key=lambda x: x['score'])

    return {"emotion": top_emotion['label']}

# Example usage
if __name__ == "__main__":
    user_message = "I feel stressed."
    emotion_result = analyze_emotion(user_message)
    print(f"Emotion: {emotion_result['emotion']}")
    print(f"sentiment: {analyze_sentiment(user_message)}")
