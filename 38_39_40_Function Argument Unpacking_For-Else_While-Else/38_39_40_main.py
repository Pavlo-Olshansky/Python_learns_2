def do_something(x, y):
    print(x, y)

coord = (21, 75)
coord_2 = {'x': 5, 'y': 6}
do_something(*coord)
do_something(**coord_2)

print([i for i in range(*coord)])

#  ------- for - else -------
my_list = [1, 2, 3, 4, 5, 6, 7]
y = 3

for x in my_list:
    if x == y:
        print('Matched ', y)
        break
else:
    print('No match')


#  ------- while - else -------

x = 0
while x < 10:
    if x > 5:
        print('x become greater than 5')
        break
    else:
        x += 11
else::
print('did not find ani example')