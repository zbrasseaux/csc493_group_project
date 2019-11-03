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
        return 'P'
    elif analysis.sentiment.polarity == 0: 
        return 'N'
    else: 
        return 'Z'
  
def get_tweets(): 
    ''' 
    function to fetch tweets and parse them. 
    '''
    # empty list to store parsed tweets
    tweets = []
    fetched_tweets = []
    file = open('MY_results_sample_data','w+')
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
            file.write(sentiment + '\n')
    file.close()
            
get_tweets()
