from population import Population
from numpy import random
from constants import TOURNAMENT_SIZE

class DuplicatesTournament:
    @staticmethod
    def select(population: Population):
        mating_pool = []
        for _ in range(len(population.chromosomes)):
            tournament = random.choice(population.chromosomes, size=TOURNAMENT_SIZE, replace=False)
            winner = max(tournament, key=lambda x: x.fitness)
            mating_pool.append(winner)
        population.update_chromosomes(mating_pool)
        return population

    
class NoDuplicatesTournament:
    @staticmethod
    def select(population: Population):
        """
        def select(population: Population, tournament_size: int):
            return deterministic_tournament_selection(population, tournament_size)
        """
        mating_pool = []
        available_chromosomes = population.chromosomes.copy()  # make a copy of chromosomes to select from
        selected_chromosomes = []  # list to keep track of chromosomes that have already been selected
        for _ in range(len(population.chromosomes)):
            remaining_chromosomes = list(set(available_chromosomes) - set(selected_chromosomes))
            if len(remaining_chromosomes) < TOURNAMENT_SIZE:  # if there are not enough remaining chromosomes for a tournament
                selected_chromosomes = []  # reset selected chromosomes and try again
                remaining_chromosomes = available_chromosomes.copy()
            tournament = random.choice(remaining_chromosomes, size=TOURNAMENT_SIZE, replace=False)
            winner = max(tournament, key=lambda x: x.fitness)
            mating_pool.append(winner)
            selected_chromosomes.extend(tournament)  # add all tournament participants to selected chromosomes

        population.update_chromosomes(mating_pool)
        return population
""" 


        mating_pool = []
        length = len(population.chromosomes)
        while len(mating_pool) < length:
            if len(population.chromosomes) < TOURNAMENT_SIZE:
                tournament = random.choice(population.chromosomes, size=len(population.chromosomes), replace=False)
            else:
                tournament = random.choice(population.chromosomes, size=TOURNAMENT_SIZE, replace=False)
            winner = max(tournament, key=lambda x: x.fitness)
            mating_pool.append(winner)
            population.chromosomes.remove(winner)

        population.update_chromosomes(mating_pool)
        return population
        """
    
"""
def deterministic_tournament_selection(population: Population):
    mating_pool = []
    for _ in range(TOURNAMENT_SIZE):
        subpopulation : Population() = population
        #subpopulation = population
        subpopulation.chromosomes = random.choice(population.chromosomes, size=len(population.chromosomes), replace=False)
        while len(subpopulation.chromosomes) > (TOURNAMENT_SIZE-1):
            tournament = random.choice(subpopulation.chromosomes, size=TOURNAMENT_SIZE, replace=False)
            winner = max(tournament, key=lambda x: x.fitness)
            subpopulation.chromosomes.remove(winner)
        mating_pool.append(subpopulation.chromosomes[0])
    
    population.update_chromosomes(mating_pool)
    return population

class NoDuplicatesTournament:
    @staticmethod
    def select(population: Population):
        new_population = population
        new_population.chromosomes = population.chromosomes.copy()
        for _ in range(TOURNAMENT_SIZE):
            deterministic_tournament_selection(new_population)
        return new_population

        """