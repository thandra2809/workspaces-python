#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# globals
d_level = 0  # manage nesting level


def main():
    r = range(11)
    l = [1, 'two', 3, {'4': 'four'}, 5]
    t = ('one', 'two', None, 'four', 'five')
    s = set("It's a bird! It's a plane! It's Superman!")
    d = dict(one=r, two=l, three=s)
    mixed = [l, r, s, d, t]
    display(mixed)


def display(o):
    global d_level

    d_level += 1
    if isinstance(o, list):
        print_list(o)
    elif isinstance(o, range):
        print_list(o)
    elif isinstance(o, tuple):
        print_tuple(o)
    elif isinstance(o, set):
        print_set(o)
    elif isinstance(o, dict):
        print_dict(o)
    elif o is None:
        print('Nada', end=' ', flush=True)
    else:
        print(repr(o), end=' ', flush=True)
    d_level -= 1

    if d_level <= 1:
        print()  # newline after outer


def print_list(o):
    print('[', end=' ')
    for x in o:
        display(x)
    print(']', end=' ', flush=True)


def print_tuple(o):
    print('(', end=' ')
    for x in o:
        display(x)
    print(')', end=' ', flush=True)


def print_set(o):
    print('{', end=' ')
    for x in sorted(o):
        display(x)
    print('}', end=' ', flush=True)


def print_dict(o):
    print('{', end=' ')
    for k, v in o.items():
        print(k, end=': ')
        display(v)
    print('}', end=' ', flush=True)


if __name__ == '__main__': main()
