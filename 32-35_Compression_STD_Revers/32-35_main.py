import numpy as np

x = [3, 4, 5, 6, 7, 8]
for i in reversed(x):
    print(i, end=' ')
y = np.array(x)
print('\n', y.std())

import zlib, sys, time, base64  # to compress / .. / .. / to encode and decode

text = open('file.txt', 'rb').read()
print('Raw size: ', sys.getsizeof(text))
#                                7 - is oprimal
compressed = zlib.compress(text, 9)  # 0-9 less_compression - more_compression
print('9 compressed size: ', sys.getsizeof(compressed))

decompressed = zlib.decompress(compressed)
print('9 compressed size: ', sys.getsizeof(decompressed))

new_text = b'Compression example with encoding'
compressed_2 = base64.b64encode(zlib.compress(new_text, 9))
print(compressed_2)
output = open('encodecomp.txt', 'wb')
output.write(compressed_2)
output.close()

read_file = open('encodecomp.txt', 'rb').read()
decompressed = zlib.decompress(base64.b64decode(read_file))
print(decompressed)
