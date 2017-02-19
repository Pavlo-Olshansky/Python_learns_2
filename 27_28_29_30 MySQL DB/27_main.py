import pymysql
import time

conn = pymysql.connect(host='localhost', user='root', password='123zxcmysql', db='begginer')  # , charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor
c = conn.cursor()
# sql='CREATE TABLE `users` (`id` int(11) NOT NULL AUTO_INCREMENT,`email` varchar(255) NOT NULL,`password` varchar(255) NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;'
# a.execute(sql)

username = 'Python'
tweet = 'man i\'m so cool'

c.execute('INSERT INTO taula (time, username, tweet) VALUES (%s, %s, %s)',
          (time.time(), username, tweet))
conn.commit()
c.execute('SELECT * FROM taula')
rows = c.fetchall()

for each_row in rows:
    print(each_row)  # each_row[2]



