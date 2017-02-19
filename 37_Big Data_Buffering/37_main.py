output = open('Output.txt', 'a')

with open('AMAT.txt', buffering=2000000) as f:  # 2 Mb ~~ 2 000 000 bytes
    for line in f:
        # print(line)
        save_to_file = line.replace('.AMAT', '')
        output.write(save_to_file)
output.close()
