#!/usr/bin/env python3
#coding=utf8
d={
    'Michael':95,
    'Bob':75,
    'Tract':85
}
print('d[\'Michael\']',d['Michael'])
print("d['Bob']",d['Bob'])
print("d.get('Tract',-1)",d.get('Tract',-1))
print("d.get('Tracts',-1)",d.get('Tracts',-1))

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k,v in d.items():
    print(k,v)