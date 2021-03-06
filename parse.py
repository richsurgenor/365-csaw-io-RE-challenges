import pandas as pd
import binascii
import numpy

#initial, i dont know why its different
#keys = [0x27,0xb3,0x73,0x9d,0xf5,0x11,0xe7,0xb1,0x0,0xb7,0xbb,0x6a,0x1c,0x6a,0x4c,0xea,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xc5,0xce,0x91,0x64,0x3f,0x7f,0x0,0x0,0x0,0x0,0x0,0x0,0x0]

#when signed long long
#keys = [0x27,0xb3,0x73,0x9d,0xf5,0x11,0xe7,0xb1,0x0,0x14,0xa,0xaa,0xb1,0x73,0xb,0x24,0x0,0xb7,0x8c,0x64,0xc2,0x55,0x0,0x0,0xe7,0x1a,0xf8,0xc2,0x7d,0x7f,0x0,0x0,0x0,0x0,0x4,0x0,0x0]

#when unsigned long long
keys = [0x27,0xb3,0x73,0x9d,0xf5,0x11,0xe7,0xb1,0x0,0x2b,0x61,0x62,0x57,0xb1,0xdc,0x95,0x0,0x77,0xd6,0xc3,0x92,0x55,0x0,0x0,0xe7,0x7a,0x93,0xba,0x10,0x7f,0x0,0x0,0x0,0x0,0x4,0x0,0x0]
#indices = data[1:data.size:2]
#values = data[2:data.size-1:2]

#for value in values:
#    print(value)
#note: we actually want the indexes as our result

#for value in values:
#    print("hi " + value)
#    value = int(value, 16)
#    value = hex(value)
#
#for index in indices:
#    index = int(index, 16)
#    index = hex(index)

#print(values)
#for key in keys:
#    print( indices[ numpy.where( values==key) ] )
    
lines = numpy.loadtxt("data.csv", delimiter=",", unpack=False)

#Only need the first line.
data = lines.astype(int).tolist()

indices = [x for ind,x in enumerate(data) if ind%2 == 0]
values = [x for ind,x in enumerate(data) if ind%2 == 1]

print(indices)
print(values)

result = []

for key in keys:
    if (int(key) == 0):
        result.append(0)
        continue
    my_index = values.index(key)
    result.append(indices[my_index])

result = [chr(x) for x in result]

print(result)
#print(indices)
#print(values)
