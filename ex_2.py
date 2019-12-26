#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = ['A', 'a', 'A', 'b', 'B']

data3 = gen_random(1, 3, 5)


print(list(Unique(data2, ignore_case=True)))
print(list(Unique(data2)))
print(list(Unique(data3)))
print(list(Unique(data1)))