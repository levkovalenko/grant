

class Tour(object):
    def __init__(self, tour=list(), good_view=True, dist_matrix=None):
        if good_view:
            self.tour = tour
        else:
            self.tour = tour.append(tour[0])
        if dist_matrix:
            self.__dist = self.calc_distance(dist_matrix)
        else:
            self.__dist = -1

    def calc_distance(self, matrix):
        dist_way = 0.
        for i in range(len(self.tour) - 1):
            dist_way += matrix[self.tour[i], self.tour[i + 1]]
        self.__dist = dist_way
        return dist_way

    @property
    def dist(self):
        return self.__dist

    def __str__(self):
        string = ""
        for town in self.tour:
            string += f"{town} "
        return string
