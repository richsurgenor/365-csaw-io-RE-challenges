import pandas as pd
import binascii
import numpy

keys = [0x27,0xb3,0x73,0x9d,0xf5,0x11,0xe7,0xb1,0x0,0xb7,0xbb,0x6a,0x1c,0x6a,0x4c,0xea,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0x0,0xc5,0xce,0x91,0x64,0x3f,0x7f,0x0,0x0,0x0,0x0,0x0,0x0,0x0]

temp_data = pd.read_csv('data.csv', dtype=str)
data = temp_data.to_numpy()

print(temp_data)

print(data.shape)
data = data.reshape( ( data.shape[0] * data.shape[1] ) )
print(data.shape)

indices = data[1:data.size:2]
values = data[2:data.size-1:2]

#for value in values:
#    print(value)
#note: we actually want the indexes as our result

for value in values:
    print("hi " + value)
    value = int(value, 16)
    value = hex(value)

for index in indices:
    index = int(index, 16)
    index = hex(index)

print(values)
for key in keys:
    print( indices[ numpy.where( values==key) ] )
    
