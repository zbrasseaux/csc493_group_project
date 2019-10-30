import pandas as pd
import sys

tweets = pd.read_csv(sys.argv[1], names=['uk', 'id', 'date_time', 'topic', 'user', 'tweet'])
scores = {'id':[], 'values':[]}

for index, row in tweets.iterrows():
	tweet = row['tweet']
	tweet_id = str(row['id'])
	word_vec = []
	for word in str(tweet).upper().split():
		word_vec.append(word)
	scores['id'].append(tweet_id)
	scores['values'].append(word_vec)

print(scores)