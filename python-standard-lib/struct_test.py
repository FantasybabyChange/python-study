import struct

i = 111
print(struct.unpack('i', struct.pack('i', i))[0])
print(struct.pack('b', i))

pack = struct.pack(">HB", int("3"), int("11"))
print(pack)

a = 1
print(isinstance(a, type([])))
a = 2
print(int(a))

a = [1, 2, 3, 4, 5, 6, 7]
print(a[5:-1])

print(struct.pack('B', 0x08))

int('1101', 2)

b1 = 0b1110001
d1 = 0x20
if b1 & (1 << 1):
    print(1)
else:
    print(0)
