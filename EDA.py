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
print('Category with highest freq is ', max_category)

min_freq = 1000000000000000
min_category = 100
for key in dic.keys():
    if dic[key] < min_freq:
        min_freq = dic[key]
        min_category = key
print('min_freq', min_freq)
print('Category with lowest freq is ', min_category)


txt_file = open('min_max_freq.txt', 'w+')
str_1 = 'max freq for category '+ str(max_category) +' is ' + str(max_freq)
str_2 = 'min freq for category '+ str(min_category) + ' is '+ str(min_freq)
txt_file.write(str_1)
txt_file.write('\n')
txt_file.write(str_2)
txt_file.close()




