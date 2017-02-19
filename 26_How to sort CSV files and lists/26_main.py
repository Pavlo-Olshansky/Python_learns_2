import csv
import operator

sample = open('my_file.txt', 'r')
sample2 = [(5, 6), (7, 1), (3, 2)]

csv1 = csv.reader(sample, delimiter=',')

sort = sorted(csv1, key=operator.itemgetter(0))
sort2 = sorted(sample2, key=operator.itemgetter(0))

print('First Sort: ')
for each_line in sort:
    print(each_line)

print('Second Sort: ')
for each_line in sort2:
    print(each_line)
