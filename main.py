'''

Welcome to BitTwit. This application tries to analyse the general sentiment about $BTC on Twitter
and predict prices based on them. It rests on the assumption that fluctuations in the positive attitude
towards $BTC relayed on social media will affect its price on market.

BitTwit comprises
1) twitter_scraper.py that scrapes 24hrs worth of bitcoin tweets at 00:00 UTC and stores them into a csv
with respective follower count.

2) pricecollect.py that pulls bitcoin price trend data from BitcoinAverage's API, minute-wise. The price data
is also stored in a csv.

3) VADER, which is a sentiment analysis library. All the scraped tweets from the previous day are fed into it
and it will assign them a "Polarity Score" that is represented by a single scalar we call "compound value".

4) SentimentStatistics.py that takes compound values from VADER, follower counts from twitter_scraper and
scales the sentiments with the follower count. After scaling, it calculates the variance, median and average
for the compound values. These are stored in daily txt files.

'''

import twitter_scraper as ts
import pricecollect as pc
import VADER
import SentimentStatistics as SenStat
import time


date = time.gmtime()

while True:
    followers = ts.scrapetwitter(date)
    pc.pull_price(date)
    compoundlist = VADER.sentiment(date)
    SenStat.analyzer(compoundlist, followers, date)

    time.sleep(86400)