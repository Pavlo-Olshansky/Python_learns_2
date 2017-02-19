import time

ITERATION = 100000

start_time = time.time()
for n in range(ITERATION):
    x = n + n
    print(x, end=' ')
print('\nTime normaly took: ', time.time() - start_time)


'''
List comprehensions no longer support the syntactic
form [... for var in item1, item2, ...].
Use [... for var in (item1, item2, ...)] instead.


range() now behaves like xrange() used to behave,
except it works with values of arbitrary size.
The latter no longer exists.
'''
