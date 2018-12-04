from random import shuffle, randint
from tour import Tour
from dist_matrix import matrix


class Population(object):
    def __init__(self, dist_matrix, number_of_towns, number_of_tours, tours=None, rg=False, chance=51):
        self.dist_matrix = dist_matrix
        self.number_of_towns = number_of_towns
        self.number_of_tours = number_of_tours
        if tours:
            self.tours = tours
        else:
            if rg:
                self.tours = self.gen_random_tours()
            else:
                self.tours = self.gen_tours(chance)

    def gen_random_tours(self):
        tours = []
        tour = [i for i in range(self.number_of_towns)]
        for i in range(self.number_of_tours):
            shuffle(tour)
            tours.append(Tour(tour=tour, good_view=False, dist_matrix=self.dist_matrix))
        return tours

    def gen_tours(self, chance):
        close_towns = [self.get_closes(self.dist_matrix[i]) for i in range(self.number_of_towns)]
        tours = []
        for i in range(self.number_of_tours):
            tour = []
            this = randint(0, self.number_of_towns-1)
            tour.append(this)
            for _ in range(self.number_of_towns-1):
                town = self.get_next_town(chance, close_towns[this], tour)
                tour.append(town)
            print(tour)
            tours.append(Tour(tour=tour, good_view=False, dist_matrix=self.dist_matrix))
        return tours

    def get_next_town(self, chance, close_towns_for_this, tour):
        chance_for_close = randint(0, 100)
        if chance_for_close < chance:
            for town in close_towns_for_this:
                if town not in set(tour):
                    return town
        else:
            next_town = randint(0, self.number_of_towns-1)
            while next_town in set(tour):
                next_town = randint(0, self.number_of_towns-1)
            return next_town

    @property
    def best_tour(self):
        best_dist = max(tour.dist for tour in self.tours)
        pos = [tour.dist for tour in self.tours].index(best_dist)
        return self.tours[pos]

    @staticmethod
    def get_closes(dist_for_towns):
        towns = [(dist, num) for num, dist in enumerate(dist_for_towns)]
        towns.sort()
        towns = [num for _, num in towns]
        return towns


if __name__ == "__main__":
    p = Population(matrix(6), 6, 60)
    print(p.best_tour)
