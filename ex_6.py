#!/usr/bin/env python3
import json
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique

path = 'data_light.json'
with open(path) as f:
    data = json.load(f)


@print_result
def f1(arg):
    return list(Unique(list(field(arg, "job-name")), ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda s: "программист" in s, arg))


@print_result
def f3(arg):
    return list(map(lambda s: s + "с опытом Python", arg))


@print_result
def f4(arg):
    prof = gen_random(100000, 200000, len(arg))
    return list(map(lambda s: '{}, зарплата {} рублей.'.format(s[0], s[1]), zip(arg, prof)))


with timer():
    f4(f3(f2(f1(data))))
