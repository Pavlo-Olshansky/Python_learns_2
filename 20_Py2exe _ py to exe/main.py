import time


def insane_func():
    x = input('Hi there, what is your name?: ')
    return x


def main():
    y = insane_func()
    print('Hello, ', y)
    print('check it out time module works')
    time.sleep(5)

main()
