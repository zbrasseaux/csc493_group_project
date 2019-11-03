#!/usr/bin/env python3

import pandas as pd
import sys
import math
from sklearn.model_selection import train_test_split

global letters
letters = 'abcdefghijklmnopqrstuvwxyz'
letters += letters.upper()
letters = list(letters)

maxlen = 140


def tf_idf_algo(tweets):
	"""Implementation of the tf_idf algorithm found here:
	http://www.tfidf.com/
	This computes a score based on how many  times the word occurs in 
	the entire set of words, as well as how many tweets it appears in.
	"""

	# create a bag of all words
	tot_bow = []


	for tweet in tweets:
		tweet = str(tweet)
		for word in tweet.split():
			if word[0] in letters:
				tot_bow.append(str(word).upper())

	# minimize the bag of words
	min_bow = set(tot_bow)

	# calculate frequency of each word
	freq = {}

	for word in tot_bow:
		try:
			freq[word] += 1
		except KeyError:
			freq[word] = 1

	# calculate term frequency (tf) of each word
	tf = {}

	for word in min_bow:
		tf[word] = freq[word]/len(tot_bow)

	# calculate inverse document frequency (idf) of each word
	idf = {}


	for word in min_bow:
		t = 0
		for tweet in tweets:
			tweet = tweet.upper()
			if word in tweet:
				t += 1
		if t != 0:
			idf[word] = math.log(math.e, (len(tweets)/t))

	# calculate final score per word
	tf_idf = {}

	for word in min_bow:
		tf_idf[word] = tf[word]/idf[word]

	# create array of scores per tweet
	scores = []
	for tweet in tweets:
		tweet_score = []
		for word in tweet.upper().split():
			try:
				tweet_score.append(tf_idf[word])
			except KeyError:
				tweet_score.append(0)
		scores.append(tweet_score)

	return scores

def pad_num(train, test, max_val = 0):
	"""Basic implementation of zero-padding
	"""

	# find max length of all tweets
	for i in train:
		if len(i) > max_val:
			max_val = len(i)
	for i in test:
		if len(i) > max_val:
			max_val = len(i)

	# pad all smaller tweets
	for i in train:
		while len(i) < max_val:
			i.append(0)
	for i in test:
		while len(i) < max_val:
			i.append(0)	

	return train, test

# read in file
data = pd.read_csv(sys.argv[1])

# split into training and testing
train, test = train_test_split(data, test_size=.35)

# retrieve only the tweets
tweets_train = train['tweet'].values
tweets_test = test['tweet'].values

test.to_csv("airline_short.csv", index=False, sep=',')

# get the tf_idf scores
train = tf_idf_algo(tweets_train)
test = tf_idf_algo(tweets_test)

# pad the arrays
train, test = pad_num(train, test)

print(train)