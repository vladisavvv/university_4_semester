#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from copy import copy

class Matrix:
    def __init__(self, array):
        self._array = copy(array)

        self._n = len(array)
        self._m = len(array[0]) - 1

    def gauss(self):
        matrix = Matrix(self._array)

        for i in range(self._n):
            temp = self._array[i][i]

            self._array[i] = [j / temp for j in self._array[i]]

            for k in range(self._n):
                if i == k:
                    continue

                for j in range(self._m + 1):
                    if j == i:
                        continue

                    self._array[k][j] -= self._array[k][i] * self._array[i][j]

                self._array[k][i] = 0

        return [self._array[i][-1] for i in range(self._n)]
