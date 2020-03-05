import struct

i = 111
print(struct.unpack('i', struct.pack('i', i))[0])
print(struct.pack('b', i))
