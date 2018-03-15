# BitTwit 
Attempt at BTC price forecasting via Twitter sentiment analysis

__dependencies:__

VADER sentiment analysis library

Tweepy (if I remember correctly)

Numpy (for sentiment statistics)

This was built during Summer 2017 with an exploratory data analysis mindset.
The program is designed to run independently on a server and to provide sentiment statistics in support of investment decisions.
There exists a crude interface with a marketplace, but I never got around actually merging the two.

**Data collection**
Every midnight the Twitter scraper collects all matching tweets (and follower counts of their authors) with certain query criteria.
Bitcoin price movements are also collected from this time.

**Data processing**
The tweets are preprocessed and fed into VADER (a NLP sentiment analysis library) that gives sentiment scores for tweets.
These are then binned with weights according to author followage.

**Visualisation**
For exploratory analysis, simple time series plots are produced. 
