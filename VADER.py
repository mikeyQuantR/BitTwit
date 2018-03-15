
def sentiment(date):

    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

    # Sentiment analysis for collected tweets
    compoundavg = 0
    posnum = 0
    negnum = 0
    analyzer = SentimentIntensityAnalyzer()
    compounds = []
    with open('./tweets/{0}_{1}_{2}.csv'.format(date.tm_mday, date.tm_mon, date.tm_year), 'r') as tweets:
        for sentence in tweets:
            vs = analyzer.polarity_scores(sentence)
            compounds.append = vs['compound']
            if vs['compound'] > 0.5:
                posnum += 1
                compoundavg += vs['compound']
            if vs['compound'] < -0.5:
                negnum += 1
                compoundavg -= vs['compound']

    with open('./sentiment/{0}_{1}_{2}.csv'.format(date.tm_mday, date.tm_mon, date.tm_year), 'w') as compounds:
        compounds.writelines(compounds)

    return compounds
