#!/usr/bin/python3
from hidden_4 import *
names = dir()
for i in names:
    if i[0] == '_':
        pass
    else:
        print('{}'.format(i))
