
import snscrape.modules.twitter as sntwitter

def buscar_tweets(termo, limite=10):
    resultados = []
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(termo).get_items()):
        if i >= limite:
            break
        resultados.append({
            "data": tweet.date.strftime('%d/%m/%Y %H:%M'),
            "usuario": tweet.user.username,
            "conteudo": tweet.content,
            "url": tweet.url
        })
    return resultados
