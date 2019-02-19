#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matrix import Matrix

def read_SLAE(file_name):
    with open(file_name, 'r') as file:
        pass

def main():
    array = read_SLAE('sample.txt')
    matrix = Matrix(array)

    print(matrix.gauss())

if __name__ == "__main__":
    main()
