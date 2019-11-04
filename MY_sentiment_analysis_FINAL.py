import re 
import textblob
from textblob import TextBlob 
import csv

def get_tweet_sentiment(tweet):  
    analysis = TextBlob(tweet) 
    if analysis.sentiment.polarity > 0: 
        return 'P'
    elif analysis.sentiment.polarity == 0: 
        return 'N'
    else: 
        return 'Z'

def get_tweets(): 
    tweets = []
    fetched_tweets = []
    file = open('MY_results_full_data','w+')
    with open('population_preprocessed_FULL.csv', encoding = 'utf8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                fetched_tweets.append(row[0])
            line_count += 1
        for tweet in fetched_tweets:
            sentiment = get_tweet_sentiment(tweet)
            file.write(sentiment)
    file.close()
            
get_tweets()
