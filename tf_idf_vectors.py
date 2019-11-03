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
	tot_bow = []

	for tweet in tweets:
		for word in tweet.split():
			if word[0] in letters:
				tot_bow.append(str(word).upper())

	min_bow = set(tot_bow)

	freq = {}

	for word in tot_bow:
		try:
			freq[word] += 1
		except KeyError:
			freq[word] = 1

	tf = {}

	for word in min_bow:
		tf[word] = freq[word]/len(tot_bow)

	idf = {}

	for word in min_bow:
		t = 0
		for tweet in tweets:
			tweet = tweet.upper()
			if word in tweet:
				t += 1
		if t != 0:
			idf[word] = math.log(math.e, (len(tweets)/t))

	tf_idf = {}

	for word in min_bow:
		tf_idf[word] = tf[word]/idf[word]

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

def pad_num(train, test):
	max_val = 0
	for i in train:
		if len(i) > max_val:
			max_val = len(i)
	for i in test:
		if len(i) > max_val:
			max_val = len(i)

	for i in train:
		while len(i) < max_val:
			i.append(0)
	for i in test:
		while len(i) < max_val:
			i.append(0)	

	return train, test

data = pd.read_csv(sys.argv[1], \
	names=['uk', 'id', 'date_time', 'topic', 'user', 'tweet'])

train, test = train_test_split(data, test_size=.35)

tweets_train = train['tweet'].values
tweets_test = test['tweet'].values

train = tf_idf_algo(tweets_train)
test = tf_idf_algo(tweets_test)

train, test = pad_num(train, test)

print(train)