import random
from genetic import fight

def tournament(cromossomes, POPULATION):
    winners = []
    for n in range(POPULATION):
        randomC1 = random.randint(0, POPULATION - 1)
        randomC2 = random.randint(0, POPULATION - 1)

        winner = fight(cromossomes[randomC1], cromossomes[randomC2])
        winners.append(winner)

    return winners
