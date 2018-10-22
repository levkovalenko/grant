import matplotlib.pyplot as plt
import numpy as np
from math import sqrt
from random import random


class BaseMethod(object):
    def __init__(self, number=10):
        self.number_of_towns = number
        self.distance_matrix = np.zeros((self.number_of_towns,self.number_of_towns))
        self.__generator()
        self.__ways = []

    def __generator(self):
        X = np.random.randint(low=100, size=(self.number_of_towns)).astype(float)
        Y = np.random.randint(low=100, size=(self.number_of_towns)).astype(float)
        for i in range(0, self.number_of_towns):
            for j in range(0, self.number_of_towns):
                if i != j:
                    self.distance_matrix[i][j] += sqrt((X[i]-X[j])**2+(Y[i]-Y[j])**2) + random()*10
                else:
                    self.distance_matrix[i][j] += np.float('inf')

    def start(self):
        for i in range(self.number_of_towns):
            self.__generate_way(i)
        for i in range(len(self.__ways)):
            way = self.__ways[i][0]
            dist = self.distance(way)
            self.__ways[i][1] = dist
        min_way = [[],float('inf')]
        for way in self.__ways:
            if way[1]<min_way[1]:
                min_way = way
        return min_way

    def __generate_way(self, ib):
        way = []
        way.append(ib)
        M = np.matrix(self.distance_matrix)
        for i in np.arange(1, self.number_of_towns, 1):
            s = []
            for j in np.arange(0, self.number_of_towns, 1):
                s.append(M[way[i - 1], j])
            way.append(s.index(min(s)))  # Индексы пунктов ближайших городов соседей
            for j in np.arange(0, i, 1):
                M[way[i], way[j]] = float('inf')
                M[way[i], way[j]] = float('inf')
        way.append(ib)
        self.__ways.append([way, -1])

    def distance(self, way):
        dist_way = 0.
        for i in range(len(way)-1):
            dist_way += self.distance_matrix[way[i],way[i+1]]
        return dist_way

    def get_distance_matrix(self):
        return self.distance_matrix

    def put_distance_matrix(self, matrix):
        self.distance_matrix = matrix

    def get_ways(self):
        return self.__ways

a = BaseMethod(4)
print(a.start())

if __name__ == '__main__':
    a = BaseMethod(4)
    print(a.start())
