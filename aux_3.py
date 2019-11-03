import pandas as pd
import matplotlib.pyplot as plt
import csv

dir_path = '/home/hotciv/Downloads/'
filename_GOP = 'GOP_REL_ONLY.csv'
filename_elec = 'judge-1377884607_tweet_product_company.csv'

dir_path_wine = '/home/hotciv/Downloads/wine-reviews/'
filename_wine = 'winemag-data-130k-v2.csv'

df = pd.read_csv(dir_path_wine + filename_wine, sep=',', index_col=False)


def word_count(lst):
    counts = dict()

    for word in lst:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# for i, row in df.iterrows():
i = 0
que = []
quant = []
dict_que = word_count(df['winery'])
for k, v in sorted(dict_que.items(), key=lambda kv: kv[1], reverse=True):
    # if i <
    # i += 1
    que.append(k)
    quant.append(v)
    # print(k + ': ' + str(v))
plt.figure()
plt.bar(que, quant)
plt.title("winery")

plt.show()

# with open(dir_path + filename_elec) as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     i = 0
#     for row in readCSV:
#         print(row)
#         break