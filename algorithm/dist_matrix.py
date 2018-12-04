from random import randint


def matrix(n=4, a=0, b=10):
    matr = []
    for _ in range(n):
        row = []
        for j in range(n):
            row.append(randint(a, b))
        matr.append(row)
    print(matr)
    return matr
