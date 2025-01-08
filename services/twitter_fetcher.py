import tweepy

# Twitter API Keys (Replace with your own keys)
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
ACCESS_TOKEN = "your_access_token"
ACCESS_SECRET = "your_access_secret"

auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
twitter_api = tweepy.API(auth)

def fetch_tweets(keyword, count=100):
    tweets = []
    try:
        for tweet in tweepy.Cursor(twitter_api.search_tweets, q=keyword, lang="en", tweet_mode="extended").items(count):
            tweets.append(tweet.full_text)
    except Exception as e:
        print(f"Error fetching tweets: {e}")
    return tweets
