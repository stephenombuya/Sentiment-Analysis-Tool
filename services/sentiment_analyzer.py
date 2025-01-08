import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(tweets):
    results = []
    for tweet in tweets:
        sentiment = sia.polarity_scores(tweet)
        if sentiment['compound'] > 0.05:
            label = 'Positive'
        elif sentiment['compound'] < -0.05:
            label = 'Negative'
        else:
            label = 'Neutral'
        results.append({'tweet': tweet, 'sentiment': label, 'scores': sentiment})
    return results
