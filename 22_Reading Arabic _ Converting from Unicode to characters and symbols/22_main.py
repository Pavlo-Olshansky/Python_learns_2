#  Deal with not only arabic, but with twitter specifically
s = u'\u0627\u0644\u0639\u062a\u0629'

encoded = s.encode('utf-8')

print(encoded)

with open('output.txt', 'wb') as file:
    file.write(encoded)
