import random
from genetic import Cromossome

def combination(cromossomes, C_SIZE, POPULATION, MIX_PROB):
    i = 0
    newGeneration = []
    while i < POPULATION:
        randomNumber = random.randint(0, 100)
        randomNumber = randomNumber / 100.0
        if randomNumber < MIX_PROB:
            C1 = cromossomes[i].getList()
            C2 = cromossomes[i+1].getList()
            newC1 = []
            newC2 = []
            randomPosition = random.randint(0, C_SIZE - 1)
            for position in range(C_SIZE):
                if position < randomPosition:
                    newC1.append(C1[position])
                    newC2.append(C2[position])
                else:
                    newC1.append(C2[position])
                    newC2.append(C1[position])
            
            newCromossome1 = Cromossome()
            newCromossome1.setCromossomeList(newC1)
            newCromossome2 = Cromossome()
            newCromossome2.setCromossomeList(newC2)
            newGeneration.append(newCromossome1)
            newGeneration.append(newCromossome2)
        else:
            newGeneration.append(cromossomes[i])
            newGeneration.append(cromossomes[i+1])
        
        i = i + 2
    
    return newGeneration