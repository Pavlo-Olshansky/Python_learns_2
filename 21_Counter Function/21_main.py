from collections import Counter

example_list = [1, 2, 4, 34, 2, 23, 65, 2, 'lol', 'lol', 'kek']

counts = Counter(example_list)
print(counts)

specific = counts[2]
print(specific)
print('No elements like this "non_exist" :', counts['non_exist'])

counts[1] = 15
counts[2] = 0  # or del counts[1]
print(counts)

x = list(counts.elements())  # y = dict(counts)
print(x)
y = counts.most_common(3)
print('TOP 3: ', y, ' Most common: ', y[0])

another_list = [1, 3, 5, 6, 7, 5, 3, 2, 1, 2]

counts_2 = Counter(another_list)
print('Another list: ', counts_2)
print('Adding: ', counts + counts_2)
print('Substraction ', counts - counts_2)


