import time
from datetime import datetime
from time import mktime

big_data_file = open('AMAT.txt', 'r')
read_file = big_data_file.read()

line_split = read_file.split('\n')

for every_line in line_split:
    divided_line = every_line.split(',')

    stock_name = divided_line[0].split('.')[1]
    initial_date = divided_line[2] + divided_line[3]
    unix_stamp = mktime(datetime.strptime(initial_date, '%Y%m%d%H%M%S').timetuple())
    date_stamp = time.strftime('%m/%d/%Y %H:%M:%S', time.localtime(unix_stamp))

    stock_price = divided_line[4]

    reformatted = unix_stamp, date_stamp, stock_name, stock_price
    save_format = str(reformatted).replace('\'', '').replace('(', '').replace(')', '')
    # print(save_format)
    # print(reformatted)

    append_file = open('example.txt', 'a')
    append_file.write(save_format)
    append_file.write('\n')
    append_file.close()


    # time.sleep(555)


