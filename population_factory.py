import math

from numpy import random
from chromosome import Chromosome
from population import Population
from coding import encode


class PopulationFactory:
    def __init__(self, fitness_function):
        self.fitness_function = fitness_function

    def generate_population(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        for j in range(start, n):
            code = random.binomial(n=1, p=.5, size=l)
            fitness = self.fitness_function.estimate(code)
            chromosomes.append(Chromosome(code, fitness, j+1))
        return Population(chromosomes, p_m)

    def generate_population_fx(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        fitness_list = random.binomial(n=self.fitness_function.b, p=.5, size=n-start)

        for y in fitness_list:
            x = round(y, 2)
            chromosomes.append(Chromosome(encode(x, self.fitness_function.a, self.fitness_function.b, l), float(x), start+1))
            start = start + 1

        return Population(chromosomes, p_m)

    def generate_population_fx2(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        fitness_list = random.binomial(n=self.fitness_function.b**2, p=.5, size=n-start)

        for y in fitness_list:
            x = round(math.sqrt(y), 2)
            chromosomes.append(Chromosome(encode(x, self.fitness_function.a, self.fitness_function.b, l), float(x**2), start+1))
            start = start + 1

        return Population(chromosomes, p_m)

    def generate_population_fx4(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        fitness_list = random.binomial(n=self.fitness_function.b**4, p=.5, size=n-start)

        for y in fitness_list:
            x = round(math.sqrt(math.sqrt(y)), 2)
            chromosomes.append(Chromosome(encode(x, self.fitness_function.a, self.fitness_function.b, l), float(x**4), start + 1))
            start = start + 1

        return Population(chromosomes, p_m)

    def generate_population_f2x2(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        fitness_list = random.binomial(n=self.fitness_function.b**2, p=.5, size=n-start)

        for y in fitness_list:
            x = round(math.sqrt(y), 2)
            chromosomes.append(Chromosome(encode(x, self.fitness_function.a, self.fitness_function.b, l), float(x**2), start + 1))
            start = start + 1

        return Population(chromosomes, p_m)

    def generate_population_f512(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        fitness_list = random.binomial(n=5.12**2, p=.5, size=n-start)

        for y in fitness_list:
            x = round(math.sqrt(5.12 ** 2 - y), 2)
            chromosomes.append(Chromosome(encode(x, -5.11, 5.12, l), math.pow(5.12, 2) - math.pow(x, 2), start + 1))
            start = start + 1

        return Population(chromosomes, p_m)

    def generate_population_f514(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        fitness_list = random.binomial(n=5.12**4, p=.5, size=n-start)

        for y in fitness_list:
            x = round(math.sqrt((math.sqrt(5.12 ** 4 - y))), 2)
            chromosomes.append(Chromosome(encode(x, -5.11, 5.12, l), math.pow(5.12, 4) - math.pow(x, 4), start + 1))
            start = start + 1

        return Population(chromosomes, p_m)
    """
    def generate_population_fe025x(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        fitness_list = random.binomial(n=math.e ** (10.23 * .25), p=.5, size=n-start)

        for y in fitness_list:
            x = round(math.log(y)/.25, 2)
            chromosomes.append(Chromosome(encode(x, 0, 10.23, l), math.pow(math.e, 10.23*.25) - math.pow(math.e, x*.25), start + 1))
            start = start + 1

        return Population(chromosomes, p_m)
    """

    def generate_population_fe025x(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)
        y_max = math.log(math.e**(10.23*0.25))
        y_list = random.uniform(0, y_max, size=n-start)
        
        for y in y_list:
            x = round(y * 10.23, 2)
            fitness = math.pow(math.e, 10.23*0.25) - math.pow(math.e, x*0.25)
            chromosomes.append(Chromosome(encode(x, 0, 10.23, l), fitness, start + 1))
            start = start + 1

        return Population(chromosomes, p_m)
    
    def generate_population_fe1x(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)
        y_max = math.log(math.e**(10.23))
        y_list = random.uniform(0, y_max, size=n-start)
        
        for y in y_list:
            x = round(y * 10.23, 2)
            fitness = math.pow(math.e, 10.23) - math.pow(math.e, x)
            chromosomes.append(Chromosome(encode(x, 0, 10.23, l), fitness, start + 1))
            start = start + 1

        return Population(chromosomes, p_m)
    
    def generate_population_fe2x(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)
        y_max = math.log(math.e**(10.23*2))
        y_list = random.uniform(0, y_max, size=n-start)
        
        for y in y_list:
            x = round(y * 10.23, 2)
            fitness = math.pow(math.e, 10.23*2) - math.pow(math.e, x*2)
            chromosomes.append(Chromosome(encode(x, 0, 10.23, l), fitness, start + 1))
            start = start + 1

        return Population(chromosomes, p_m)

    def generate_population_fhd(self, n, l, p_m, i):
        if i < 5 or p_m == 0:
            chromosomes = [self.fitness_function.generate_optimal(l)]
        else:
            chromosomes = []
        start = len(chromosomes)

        for j in range(start, n):
            code = random.binomial(n=1, p=.5, size=l)
            fitness = self.fitness_function.estimate(code)
            chromosomes.append(Chromosome(code, fitness, j+1))
        return Population(chromosomes, p_m)
#%%
