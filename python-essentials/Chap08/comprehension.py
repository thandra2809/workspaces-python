#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq]
    print_list(seq)
    print_list(seq2)


def print_list(o):
    for x in o:
        print(x, end=' ')
    print()


if __name__ == '__main__': main()
