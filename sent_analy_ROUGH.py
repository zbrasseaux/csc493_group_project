import re
# import tweepy
# rom tweepy import OAuthHandler
import textblob
from textblob import TextBlob
import csv

dir_path = '/home/hotciv/Downloads/trainingandtestdata/'
filename_sample = "testdata.manual.2009.06.14.csv"


def get_tweet_sentiment(self, tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(self.clean_tweet(tweet))
    # set sentiment
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'


def get_tweets():
    ''' 
    Main function to fetch tweets and parse them. 
    '''
    # empty list to store parsed tweets
    tweets = []
    fetched_tweets = []
    # open('twitter dataset sample.csv', 'w').close()
    with open(dir_path + filename_sample) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            print('tweet #' + str(row[0]) + ': ' + str(row[5]))
            fetched_tweets.append(row[5])
            # fetched_tweets[line_count] = row[5]
            line_count += 1
        print(f'Processed {line_count} lines.')


def print_results():
    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100 * len(ptweets) / len(tweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100 * len(ntweets) / len(tweets)))
    # percentage of neutral tweets
    print("Neutral tweets percentage: {} % \ ".format(100 * len(tweets - ntweets - ptweets) / len(tweets)))


def main():
    get_tweets()
    # get_tweet_sentiment()
    # print_results()


main()