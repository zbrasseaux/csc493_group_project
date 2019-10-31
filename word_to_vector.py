import sys
from tensorflow import keras

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

import nltk
import numpy as np
import pandas as pd


def text_to_numbers(text, cutoff_for_rare_words=1):
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
    df_fdist['word_index'] = list(np.arange(number_of_words) + 1)

    # replace rare words with index zero
    frequency = df_fdist['Frequency'].values
    word_index = df_fdist['word_index'].values
    mask = frequency <= cutoff_for_rare_words
    word_index[mask] = 0
    df_fdist['word_index'] = word_index

    # Convert pandas to dictionary
    word_dict = df_fdist['word_index'].to_dict()

    # Use dictionary to convert words in text to numbers
    text_numbers = []
    for string in text:
        string_numbers = [word_dict[word] for word in string]
        text_numbers.append(string_numbers[0])

    return text_numbers


# set parameter:
maxlen = 300

dir_path = '/home/hotciv/Downloads/trainingandtestdata/'
filename_sample = "testdata.manual.2009.06.14.csv"

print('Loading data...')
# data = pd.read_csv(sys.argv[1], names=['uk', 'id', 'date_time', 'topic', 'user', 'tweet'])
data = pd.read_csv(dir_path + filename_sample)
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
    # post_tweet = [number for sublist in pst_tweet for number in sublist]
    # post_tweet = keras.preprocessing.sequence.pad_sequences(post_tweet, maxlen=maxlen)
    x_test_post.append(post_tweet)

for tweet in x_test:
    tweet = str(tweet)
    post_tweet = text_to_numbers(tweet)
    # post_tweet = [number for sublist in pst_tweet for number in sublist]
    # post_tweet = keras.preprocessing.sequence.pad_sequences(post_tweet, maxlen=maxlen)
    x_test_post.append(post_tweet)

x_test_post = keras.preprocessing.sequence.pad_sequences(x_test_post, maxlen=maxlen)

print(len(x_test_post))
n = int(input("Index: "))
# print(len(x_test_post[n][0]))
print(len(x_test_post[n]))
print(x_test_post[n])
plt.plot(x_test_post[n])
plt.show()
