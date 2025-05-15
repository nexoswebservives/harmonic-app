from services.twitter_service import buscar_tweets_por_termo

tweets = buscar_tweets_por_termo("OpenAI")
for t in tweets:
    print(t)
