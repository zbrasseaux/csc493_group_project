import re
import pandas as pd

dir_path_airline = '/home/hotciv/Downloads/twitter-airline-sentiment/'
filename_airline = 'Tweets.csv'

dir_path_wine = '/home/hotciv/Downloads/wine-reviews/'
filename_wine = 'winemag-data-130k-v2.csv'


fwr = dir_path_wine + filename_wine
fww = dir_path_wine + 'wine_formatted.csv'

far = dir_path_airline + filename_airline
faw = dir_path_airline + 'airline_formatted.csv'


df = pd.read_csv(fwr, sep=',', index_col=False)
w = open(fww, 'w')


# 6 standard fields:
#   1. polarity
#   2. id
#   3. date
#   4. query
#   5. user
#   6. tweet
for i, row in df.iterrows():
    formatted = []
    # print(row)

    # 1. polarity
    if row[4] < 88:
        formatted.append(0)
    elif row[4] > 87 and row[4] < 94:
        formatted.append(2)
    else:
        formatted.append(4)

    # 2. id (using title, as it is the most approximate of it)
    formatted.append(row[11])

    # 3. date (using Country as it doesn't have date...)
    formatted.append(row[1])

    # 4. query
    formatted.append(row[12])

    # 5. user
    formatted.append(row[10])

    # 6. tweet
    formatted.append(row[2])

    w.writelines(["\"%s\"," % item for item in formatted])
    w.write('\n')

w.close()

df = pd.read_csv(far, sep=',', index_col=False)
w = open(faw, 'w')

# 6 standard fields:
#   1. polarity
#   2. id
#   3. date
#   4. query
#   5. user
#   6. tweet
for i, row in df.iterrows():
    formatted = []

    # 1. polarity
    if row[1] == 'positive':
        formatted.append(4)
    elif row[1] == 'neutral':
        formatted.append(2)
    else:
        formatted.append(0)

    # 2. id
    formatted.append(row[0])

    # 3. date
    formatted.append(row['tweet_created'])

    # 4. query
    formatted.append(row['airline'])

    # 5. user (timezone)
    formatted.append(row['user_timezone'])

    # 6. tweet
    formatted.append(re.sub('\n', ' ', re.sub('\"', '\'', row['text'])))

    w.writelines(["\"%s\"," % item for item in formatted])
    w.write('\n')

w.close()
