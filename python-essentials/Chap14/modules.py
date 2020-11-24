#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import os


def main():
    v = os.getenv('PATH').split(':')
    print(v)


if __name__ == '__main__':
    main()
