import os
import time


def file_open(name):
    try:
        os.startfile(name)
    except Exception as e:
        print(str(e))


def close_file(name):
    try:
        os.system('TASKKILL /F /IM ' + str(name))  # os.system('TASKKILL /IM ' + str(name))  - NOT Force closing
    except Exception as e:
        print(str(e))

#        (r'simple_folder\open_me.txt')
file_open(r'C:\Users\Pavlo\Desktop\Python\Intermediate Python - sentdex\2_Python2. 2013\9_Rename and Move Files\move_me.txt')
time.sleep(3)
close_file('notepad.exe')

#  ------------------ 16 ------------
# It's perhaps only to Python 2.7
# import SendKeys
#
#
# def main():
#     try:
#         send_me = 'Hello'
#         time.sleep(2)
#         SendKeys.SendKeys(send_me)
#
#     except Exception as e:
#         print(str(e))
#
#
# if __name__ == '__main__':
#     main()
