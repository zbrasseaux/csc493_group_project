import pandas as pd
import numpy as np
import sys

from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.layers import Embedding
from keras.layers import Conv1D, GlobalMaxPooling1D
from keras.datasets import imdb

from tensorflow import keras
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import nltk
import numpy as np
import pandas as pd

def text_to_numbers(text, cutoff_for_rare_words = 1):
    """Function to convert text to numbers. Text must be tokenzied so that
    test is presented as a list of words. The index number for a word
    is based on its frequency (words occuring more often have a lower index).
    If a word does not occur as many times as cutoff_for_rare_words,
    then it is given a word index of zero. All rare words will be zero.
    """
    
    # Flatten list if sublists are present
    if len(text) > 1:
        flat_text = [item for sublist in text for item in sublist]
    else:
        flat_text = text
    
    # get word freuqncy
    fdist = nltk.FreqDist(flat_text)

    # Convert to Pandas dataframe
    df_fdist = pd.DataFrame.from_dict(fdist, orient='index')
    df_fdist.columns = ['Frequency']

    # Sort by word frequency
    df_fdist.sort_values(by=['Frequency'], ascending=False, inplace=True)

    # Add word index
    number_of_words = df_fdist.shape[0]
    df_fdist['word_index'] = list(np.arange(number_of_words)+1)

    # replace rare words with index zero
    frequency = df_fdist['Frequency'].values
    word_index = df_fdist['word_index'].values
    mask = frequency <= cutoff_for_rare_words
    word_index[mask] = 0
    df_fdist['word_index'] =  word_index
    
    # Convert pandas to dictionary
    word_dict = df_fdist['word_index'].to_dict()
    
    # Use dictionary to convert words in text to numbers
    text_numbers = []
    for string in text:
        string_numbers = [word_dict[word] for word in string]
        text_numbers.append(string_numbers)  
    
    return (text_numbers)

# set parameters:
max_features = 5000
maxlen = 140
batch_size = 32
embedding_dims = 50
filters = 250
kernel_size = 3
hidden_dims = 250
epochs = 2

print('Loading data...')
data = pd.read_csv(sys.argv[1], names=['uk', 'id', 'date_time', 'topic', 'user', 'tweet'])
train, test = train_test_split(data, test_size=.35)

print(train)
print(test)

x_train = train['tweet'].values.tolist()
x_test = test['tweet'].values.tolist()

print(len(x_train), 'train sequences of type ' + str(type(x_train)))
print(len(x_test), 'test sequences of type ' + str(type(x_test)))

x_train_post = []
x_test_post = []

for tweet in x_train:
	tweet = str(tweet)
	post_tweet = text_to_numbers(tweet)
	post_tweet = keras.preprocessing.sequence.pad_sequences(post_tweet, maxlen=maxlen)
	x_test_post.append(post_tweet)

for tweet in x_test:
	tweet = str(tweet)
	post_tweet = text_to_numbers(tweet)
	post_tweet = keras.preprocessing.sequence.pad_sequences(post_tweet, maxlen=maxlen)
	x_test_post.append(post_tweet)

print(len(x_test_post))
