with open('input/lanternfish.txt') as f:
    ages = [line.rstrip() for line in f]

population = [int(a) for a in ages[0].split(',')]

def aging_process(population,days):

    if days == 0:
        return population

    newborn = []

    for i,fish in enumerate(population):
        if fish == 0:
            population[i] = 6
            newborn.append(8)
        else:
            population[i] -= 1

    population.extend(newborn)

    return aging_process(population,days-1)

def increase_population(fish_per_age):
    new_population = [0] * 9
    for i,fish in enumerate(fish_per_age[1:]):
        new_population[i] += fish

    new_population[6] += fish_per_age[0]
    new_population[8] += fish_per_age[0]

    return new_population

def longer_times(population,days):
    fish_per_age = [0] * 9
    for fish in population:
        fish_per_age[fish] += 1
    
    #print(fish_per_age)
    
    for day in range(days):
        fish_per_age = increase_population(fish_per_age)
        #print(fish_per_age,sum(fish_per_age))

    return sum(fish_per_age)

population = [int(a) for a in ages[0].split(',')]
final_pop = aging_process(population,80)
pop_size = len(final_pop)

print(f'After 80 days the population has grown to {pop_size}')

population = [int(a) for a in ages[0].split(',')]
total_population = longer_times(population,256)
print(f'After 256 days the population has grown to {total_population}')
    