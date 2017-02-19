sample_file = open('small_arabic.csv', 'r').read()
split_file = sample_file.split('n')
arabic_text = split_file[8].split(' ')
print(arabic_text, len(arabic_text[:]))

for i in range(len(arabic_text[:]) - 1):
    x = arabic_text[i+1].encode('utf-8')
    print(x.decode('unicode-escape'), end=' ')

