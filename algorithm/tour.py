from random import randint


class Tour(object):
    def __init__(self, tour=list(), good_view=True, dist_matrix=None):
        if good_view:
            self.tour = tour
        else:
            self.tour = tour
            self.tour.append(tour[0])
        if dist_matrix:
            self.calc_distance(dist_matrix)
        else:
            self.__dist = -1

    def calc_distance(self, matrix):
        dist_way = 0.
        for i in range(len(self.tour) - 1):
            dist_way += matrix[self.tour[i]][self.tour[i + 1]]
        self.__dist = dist_way

    @property
    def dist(self):
        return self.__dist

    def __str__(self):
        string = ""
        for town in self.tour:
            string += f"{town} -> "
        return string

    @classmethod
    def crossover(cls, p_tour1, p_tour2, cross_len=3):
        child = p_tour1
        number_of_towns = len(p_tour1)
        pos = randint(0,number_of_towns-cross_len-1)
        new_towns = set()
        old_towns = set()
        for i in range(pos, cross_len+pos):
            old_towns.add(child[i])
            new_towns.add(p_tour2[i])
            child[i] = p_tour2[i]
        towns_to_add = old_towns - new_towns
        towns_to_delet = new_towns - old_towns
        for town_add, town_del in list(zip(list(towns_to_add), list(towns_to_delet))):
            child[child.index(town_del)] = town_add
        return Tour(child, False)

    @classmethod
    def mutation(cls, child):
        a = randint(0, len(child)-1)
        b = randint(0, len(child)-1)
        while a == b:
            a = randint(0, len(child))
            b = randint(0, len(child))
        child[a], child[b] = child[b], child[a]
        return Tour(child, False)


if __name__ == "__main__":
    print(Tour.crossover([1, 2, 3, 4, 5, 6, 7, 8], [5,6,8,3,7,2,4,1],4))
    print(Tour.mutation([1, 2, 3, 4, 5, 6, 7, 8]))
