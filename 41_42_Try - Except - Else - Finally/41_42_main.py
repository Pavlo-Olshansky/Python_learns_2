try:
    x = 3 + 3
except:
    x = 4 + 4
else:
    x += 1
finally:
    print('do smth else with x = ', x)
