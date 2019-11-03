from random import random, randint

def fitness(data):
    return (data['serviced']['regular']/(data['total']['regular'] + 1)) * (data['total']['attacker']/(data['serviced']['attacker'] + 1))

def evaluate(id, results, vhm):
    from emulator import emulator
    data = emulator(vhm)
    results[id] = fitness(data)

def genetic_algorithm():
    population_size = 5
    max_crossovers = 2
    max_mutations = 2

    # initialize close to 0 so that initiallly all requests are serviced
    population = [random()/10 - 0.05 for _ in range(population_size)]


    while True:
        # initialize empty list to hold results
        fitness = ([0] * population_size).copy()
        
        print('population', population)

        for i in range(population_size):
            evaluate(i, fitness, population[i])
        
        print('max fitness', max(fitness))
        for i in range(population_size):
            if fitness[i] == max(fitness):
                print('vhm corresponding to max population', population[i])
                break

        # calculate sum for normalization
        s = sum(fitness)

        # normalize the fitness values
        for i in range(population_size):
            fitness[i] /= s
        

        for i in range(1, len(fitness)):
            fitness[i] += fitness[i-1]

        selected = [None] * population_size

        for i in range(population_size):
            r = random()
            for j in range(population_size):
                if fitness[j] >= r:
                    selected[i] = population[j]
                    break

        no_of_crossovers = randint(0, max_crossovers)
        for _ in range(no_of_crossovers):
            c1 = randint(0, population_size - 1)
            c2 = randint(0, population_size - 1)

            selected[c1] = (selected[c1] + selected[c2]) / 2

        no_of_mutations = randint(0, max_mutations)
        for _ in range(no_of_mutations):
            r = randint(0, population_size - 1)
            selected[r] += selected[r] * ( 2 * random())
        
        population = selected

if __name__ == "__main__":
    genetic_algorithm()