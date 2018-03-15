import tweepy
import csv
import time


# Necessary API keys and secrets
consumer_key = 
consumer_secret = 
access_token = 
access_secret = 


def scrapetwitter(date):
    # Setting rights
    auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    if not api:
        print('You botched the authentication!')
        exit()

    # Query parameters
    query = 'bitcoin%20OR%20btc'
    maxTweets = 100000      # Large enough to capture every tweet from a particular day
    tweetsPerQry = 100

    sinceId = None
    max_id = -1

    tweetCount = 0
    print("Downloading max {0} tweets...".format(maxTweets))

    fcountlist = []
    with open('.\ tweets\{0}_{1}_{2}.csv'.format(date.tm_year, date.tm_mon, date.tm_mday), 'w') as tweets:
        tweetwrit = csv.writer(tweets, lineterminator='\n')
        while tweetCount < maxTweets:
            try:
                if max_id <= 0:
                    if not sinceId:
                        new_tweets = api.search(q=query, lang='en', count=tweetsPerQry, since='2017-07-26',
                                                    until='2017-07-27')
                    else:
                        new_tweets = api.search(q=query, lang='en', count=tweetsPerQry,
                                                    since_id=sinceId, since='2017-07-26', until='2017-07-27')
                else:
                    if not sinceId:
                        new_tweets = api.search(q=query, lang='en', count=tweetsPerQry,
                                                    max_id=str(max_id-1), since='2017-07-26', until='2017-07-27')
                    else:
                        new_tweets = api.search(q=query, lang='en', count=tweetsPerQry,
                                                    max_id=str(max_id-1),
                                                    since_id=sinceId, since='2017-07-26', until='2017-07-27')
                if not new_tweets:
                    print('End of Everything!')
                    break
                for s in new_tweets:
                    text = s.text
                    if 'Casino' in text:
                        pass
                    time = s.created_at
                    text = ''.join([i if ord(i) < 128 else ' ' for i in text])
                    fcount = s.user.followers_count
                    fcountlist.append(fcount)
                    tweetwrit.writerow(['{0},{1},{2}'.format(time, fcount, text)])
                tweetCount += len(new_tweets)
                print('Downloaded {0} shitposts'.format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                print("Get rekt with:" + str(e))
                break

    return fcountlist
