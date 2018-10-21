import numpy as np


class test:
    def __init__(self, s, matrix, n0):
        self.s = s
        self.t = None
        self.matrix = matrix
        self.n0 = n0

    def sm(self, t):
        """
        s- из статьи
        :param t:int текущее "время"
        :return:list пройденный путь
        """
        return self.s[0:int(self.n0 * t / T) + 1]

    def sp(self, t):
        """
        s+ из статьи
        :param t:int текущее "время"
        :return:list оставшийся путь
        """
        return self.s[int(self.n0 * t / T):len(s) - 1]

    def f(self):
        """
        целевая функция
        :return:int "стоимость" пути
        """
        out = 0
        for i in range(1, len(self.s)):
            out += self.matrix[self.s[i - 1]][self.s[i]]
        return out

    def __lt__(self, other):
        """
        перегрузка оператора <
        :param other: второй операнд
        :return:
        """
        return self.f() < other.f()

    def __gt__(self, other):
        """
        перегрузка оператора >
        :param other: второй операнд
        :return:
        """
        return self.f() > other.f()

    def get_error(self, t):
        """
        функция, которую можно вызывать при получении неустойчивости
        :param t:int время сбоя
        :return: None
        """
        self.t = t




def generate_task(s, matrix):
    """
    создание новой задачи по городам из маршрута s
    :param s:list путь
    :param matrix:np.array матрица расстояний для пути s
    :return:np.array новая матрица расстояний
    """
    new_matrix = np.empty((len(set(s)), len(set(s))))
    temp = list(set(s))
    temp.sort()
    for i in range(len(temp)):
        for j in range(len(temp)):
            new_matrix[i][j] = matrix[s[i]][s[j]]
    return new_matrix


if __name__ == '__main__':
    T = 5  # параметр
    M = 5  # параметр
    # matrix = [] # здесь должна быть матрица длин задачи
    matrix = np.array([None, 10, 25, 25, 10,
                       1, None, 10, 15, 2,
                       8, 9, None, 20, 10,
                       14, 10, 24, None, 15,
                       10, 8, 25, 27, None])
    matrix = matrix.reshape((5, 5))
    # сие есть отладочный костыль (напишешь интерфейс - будем адаптировать)

    n0 = matrix.shape[0]  # если она квадратная
    s = [i for i in range(n0)]  # сие есть отладочный костыль (напишешь интерфейс - будем адаптировать)
    s.append(0)  #
    obj = test(s, matrix, n0)

    b_list = list([0 for i in range(1, T)])  # количество рухнувших на каждой итерации

    for i in range(M):
        # s = generate_new_way(matrix)
        for j in range(0, T-1):
            # s_new = obj.sm(i)[0:(len(obj.sm(i)) - 1)] + generate_new_way(generate_task(sp(i, s), matrix))
            s_new = [0, 4, 1, 2, 3, 0] # сие есть отладочный костыль (напишешь интерфейс - будем адаптировать)
            obj_new = test(s_new, matrix, n0)
            if obj > obj_new:
                b_list[j] += 1
                break