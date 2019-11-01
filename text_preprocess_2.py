import re
import csv
import nltk
import unicodedata
import contractions
import pandas as pd

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# Convert a list to string using join() function
def list_to_string(s):
    # initialize an empty string
    str1 = " "

    # return string
    return str1.join(s)


def file_len(fname):
    with open(fname, 'r') as f:
        for j, l in enumerate(f):
            pass
        return j + 1


def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words


def remove_return(text):
    return re.sub('\n', ' ', text)


dir_path = '/home/hotciv/Downloads/trainingandtestdata/'
filename_sample = "testdata.manual.2009.06.14.csv"
filename_population = 'training.1600000.processed.noemoticon.csv'

dir_path_airline = '/home/hotciv/Downloads/twitter-airline-sentiment/'
filename_airline = 'airline_formatted.csv'

dir_path_wine = '/home/hotciv/Downloads/wine-reviews/'
filename_wine = 'wine_formatted.csv'

lemmatizer = WordNetLemmatizer()

opt = input('Sample, population, wine or airline [s/p/w/a]? ')
if opt == 's':
    f = dir_path + filename_sample
    f2 = dir_path + 'sample-test_prepocessed.csv'
    tam = file_len(f2)
    print("Size of the file so far: %s", str(tam))
    w = open(f2, 'a+')
elif opt == 'p':
    f = dir_path + filename_population
    f2 = dir_path + 'population_prepocessed.csv'
    tam = file_len(f2)
    print("Size of the file so far: %s", str(tam))
    w = open(f2, 'a+')
elif opt == 'w':
    f = dir_path_wine + filename_wine
    f2 = dir_path_wine + 'wine_preprocessed.csv'
    w = open(f2, 'w')
elif opt == 'a':
    f = dir_path_airline + filename_airline
    f2 = dir_path_airline + 'airline_preprocessed.csv'
    w = open(f2, 'w')


print("Contnuing the work...")

# df = pd.read_csv(f, sep=',')  # , index_col=False)
f1 = open(f)
readCSV = csv.reader(f1, delimiter=',')

# Make own character set and pass
# this as argument in compile method
# regex = re.compile('[,._!$%^&*()<>?/\|}{~:;\'\"]')
regex = re.compile('\W')

for row in readCSV:
    row = row[:6]
# for i, row in df.iterrows():

    # if i >= tam:

    # 'expand' the tweet
    sample = contractions.fix(row[5])
    # print(row[5])
    # print(sample)

    # # replace '\n' by ' '
    # sample = remove_return(sample)
    # print(sample)
    # sample = ''.join(sample)
    # print(sample)
    # print(type(sample))
    # input()

    # turn the tweet into a list of words and symbols
    words = nltk.word_tokenize(sample)
    words = remove_non_ascii(words)
    len_words = len(words)
    # print(words)
    fixed = []
    k = 0

    ####### preprocess the text #######

    # for each token
    while k < len_words:

        # get the users and hashtags
        if words[k] == '@' or words[k] == '#':
            if k + 1 < len_words:
                fixed.append(words[k] + words[k + 1])
                k += 1

        elif words[k] == 'http' or words[k] == 'https':
            if k + 2 < len_words:
                link = words[k] + words[k+1] + words[k+2]
                fixed.append(link)
                k += 2
            else:
                fixed.append(words[k])
            # if k + 1 < len_words:
            #     print(str(i + 1) + ' - ' + link)
            #     print(words[k+1])

        # try to reconstruct ASCII emojis
        elif regex.search(words[k]) != None:
            to_append = words[k]
            while k + 1 < len_words and regex.search(words[k]) != None and len(words[k+1]) == 1 and regex.search(words[k+1]) != None:
                to_append = to_append + words[k+1]
                k += 1
            if len(to_append) != 1:
                fixed.append(to_append)
            elif to_append == '?':
                fixed.append(to_append)

        # if nothing has to be done
        # lemmatize the lowercase word
        # and, if it isn't a stopword, 'save' it
        else:
            lemma = lemmatizer.lemmatize(words[k].lower(), pos='v')

            # negative words that are on the stopwords.words('english') but should be kept
            if lemma == 'no' or lemma == 'nor' or lemma == 'not':
                fixed.append(lemma)
            elif lemma not in stopwords.words('english'):
                fixed.append(lemma)
        k += 1
        ####### preprocess the text #######


    # write it to the file
    row[5] = list_to_string(fixed)
    w.writelines(["\"%s\"," % item for item in row])
    w.write('\n')

    # print(fixed)
