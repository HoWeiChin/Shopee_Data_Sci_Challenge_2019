import pandas as pd 
import os
import matplotlib.pyplot as plt

curr_dir = os.getcwd()
data_dir = os.path.join(curr_dir, 'train.csv')
print('data_dir', data_dir)

csv = pd.read_csv(data_dir)
print('column names are: ' + str(list(csv)))

#only titles and Category columns are interesting
csv.loc[:, 'title'].head()
csv.loc[:, 'Category'].head()

#for plotting histogram

dic = {}
#store item category as key, count of a category as a value
for cat in csv.loc[:, 'Category']:
    if cat not in dic:
        dic[cat] = 1
    else:
        dic[cat] += 1

#histogram
x_val = list(dic.keys())
y_val = list(dic.values())
plt.title('Category Frequencies Distribution')
plt.xlabel('Category Type')
plt.ylabel('Frequency')
plt.bar(x_val, y_val, color='g')
plt.show()

max_freq = -1
max_category = 100
for key in dic.keys():
    if dic[key] > max_freq:
        max_freq = dic[key]
        max_category = key
print('max_freq', max_freq)
print('Category with highest freq', max_category)




