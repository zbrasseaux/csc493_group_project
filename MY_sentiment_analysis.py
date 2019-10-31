import re 
import textblob
from textblob import TextBlob 
import csv
  
def get_tweet_sentiment(tweet): 
    ''' 
    Utility function to classify sentiment of passed tweet 
    using textblob's sentiment method 
    '''
    # create TextBlob object of passed tweet text 
    analysis = TextBlob(tweet) 
    # set sentiment 
    if analysis.sentiment.polarity > 0: 
        return 'positive'
    elif analysis.sentiment.polarity == 0: 
        return 'neutral'
    else: 
        return 'negative'
  
def get_tweets(): 
    ''' 
    function to fetch tweets and parse them. 
    '''
    # empty list to store parsed tweets
    tweets = []
    fetched_tweets = []
    file = open('result.csv','w+')
    with open('twitter dataset sample.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            fetched_tweets.append(row[5])
            line_count += 1
        #print(f'Processed {line_count} lines.')
        for tweet in fetched_tweets:
            sentiment = get_tweet_sentiment(tweet)
            #print(sentiment)
            file.write(sentiment + ',')
    file.close()
            
get_tweets()
