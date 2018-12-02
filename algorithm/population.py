from random import shuffle, randint
from algorithm.tour import Tour


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
                self.tours = self.gen_tours(51)

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
            this = randint(0, self.number_of_towns)
            tour.append(this)
            for _ in range(self.number_of_towns-1):
                town = self.get_next_town(chance, close_towns[this], tour)
                tour.append(town)
            tours.append(Tour(tour=tour, good_view=False, dist_matrix=self.dist_matrix))
        return tours

    def get_next_town(self, chance, close_towns_for_this, tour):
        chance_for_close = randint(0, 100)
        if chance_for_close < chance:
            for town in close_towns_for_this:
                if town not in tour:
                    return town
        else:
            next_town = randint(0, self.number_of_towns)
            while next_town not in tour:
                next_town = randint(0, self.number_of_towns)
            return next_town

    @staticmethod
    def get_closes(dist_for_towns):
        towns = [(dist, num) for num, dist in enumerate(dist_for_towns)]
        towns.sort()
        return towns
