import random
from genetic import Cromossome

def mutation(newGeneration, MUT_PROB, C_SIZE, C_RANGE):
    for element in newGeneration:
        randomNumber = random.randint(0, 100)
        randomNumber = randomNumber / 100.0
        if randomNumber < MUT_PROB:
            randomPosition = random.randint(0, C_SIZE - 1)
            newValue = random.randint(0, C_RANGE - 1)
            element.changeCromossomeAtPosition(randomPosition, newValue)