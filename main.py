#!python
from math import sin, cos, sqrt, isnan, isinf
import pandas
import random
from grammar import Grammar
from genetic import Cromossome, fight

# Open .csv file and import it in a dictionary structure
#data = pandas.read_csv("csv-files/reduced.csv")
data = pandas.read_csv("csv-files/training.csv")

# Genetic parameters
C_SIZE = 20
POPULATION = 1000 # Must be an even number
C_RANGE = 20
MIX_PROB = 0.8
MUT_PROB = 0.1
NUM_GENERATIONS = 10

# Initialize grammar
grammar = Grammar()
grammar.setVariables(data.keys()[0:-1])


# Initial cromossomes
cromossomes = []
for n in range(POPULATION):
  C = Cromossome()
  C.setRandomList(C_SIZE, C_RANGE)
  cromossomes.append(C)

for generation in range(NUM_GENERATIONS):
  message = "\n---- Generation: " + str(generation) + " ----"
  print(message)
  # Convert cromossomes to expressions
  for C in cromossomes:
    C.setExpression(grammar.cromossomeToExpression(C))


  # Evaluate cromossomes scores

  # Calculate multiplier constant
  for C in cromossomes:
    mathErrorFlag = False
    avgMultiplier = 0
    count = 0

    for row in data.ID:
      ID = data.ID[count]
      Cement = data.Cement[count]
      Blasr = data.Blasr[count]
      FlyAsh = data.FlyAsh[count]
      Water = data.Water[count]
      Superplasticizer = data.Superplasticizer[count]
      CoarseAggregate = data.CoarseAggregate[count]
      FineAggregate = data.FineAggregate[count]
      Age = data.Age[count]

      try:
        calculated = eval(C.getExpression())
        multiplier = abs(data.strength[count] / calculated)
        if isnan(multiplier) or isinf(multiplier):
          multiplier = 1
      except:
        mathErrorFlag = True
        calculated = 0
        multiplier = 1
      
      avgMultiplier = avgMultiplier + multiplier
      count = count + 1
    
    avgMultiplier = avgMultiplier / count
    C.setMultiplier(avgMultiplier)

  # Evaluate expression
  for C in cromossomes:
    mathErrorFlag = False
    avgScore = 0
    count = 0

    for row in data.ID:
      ID = data.ID[count]
      Cement = data.Cement[count]
      Blasr = data.Blasr[count]
      FlyAsh = data.FlyAsh[count]
      Water = data.Water[count]
      Superplasticizer = data.Superplasticizer[count]
      CoarseAggregate = data.CoarseAggregate[count]
      FineAggregate = data.FineAggregate[count]
      Age = data.Age[count]

      try:
        calculated = eval(C.getExpression())
      except:
        mathErrorFlag = True
        calculated = 0
      score = (data.strength[count] - avgMultiplier * calculated) ** 2
      
      avgScore = avgScore + score
      count = count + 1
    
    avgScore = avgScore / count
    if isnan(avgScore) or mathErrorFlag:
      avgScore = 999999999
    C.setScore(avgScore)

  min_score = cromossomes[0].getScore()
  min_index = 0
  index = 0
  for C in cromossomes:
    if C.getScore() < min_score:
      min_index = index
      min_score = C.getScore()
    index = index + 1

  print(str(cromossomes[min_index].getMultiplier()) + " * " + cromossomes[min_index].getExpression())
  print("Score: " + str(cromossomes[min_index].getScore()))


  # Tournament
  winners = []
  for n in range(POPULATION):
    randomC1 = random.randint(0, POPULATION - 1)
    randomC2 = random.randint(0, POPULATION - 1)

    winner = fight(cromossomes[randomC1], cromossomes[randomC2])
    winners.append(winner)

  # Genetic combination
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

  # Mutation
  for element in newGeneration:
    randomNumber = random.randint(0, 100)
    randomNumber = randomNumber / 100.0
    if randomNumber < MUT_PROB:
      randomPosition = random.randint(0, C_SIZE - 1)
      newValue = random.randint(0, C_RANGE - 1)
      element.changeCromossomeAtPosition(randomPosition, newValue)

  cromossomes = newGeneration


# Last generation selection

for C in cromossomes:
    C.setExpression(grammar.cromossomeToExpression(C))

# Evaluate cromossomes scores
for C in cromossomes:
  mathErrorFlag = False
  avgScore = 0
  count = 0

  for row in data.ID:
    ID = data.ID[count]
    Cement = data.Cement[count]
    Blasr = data.Blasr[count]
    FlyAsh = data.FlyAsh[count]
    Water = data.Water[count]
    Superplasticizer = data.Superplasticizer[count]
    CoarseAggregate = data.CoarseAggregate[count]
    FineAggregate = data.FineAggregate[count]
    Age = data.Age[count]

    try:
      calculated = eval(C.getExpression())
    except:
      mathErrorFlag = True
      calculated = 0
    score = (data.strength[count] - calculated) ** 2
    
    avgScore = avgScore + score
    count = count + 1
  
  avgScore = avgScore / count
  if isnan(avgScore) or mathErrorFlag:
    avgScore = 999999999
  C.setScore(avgScore)

min_score = cromossomes[0].getScore()
min_index = 0
index = 0
for C in cromossomes:
  if C.getScore() < min_score:
    min_index = index
    min_score = C.getScore()
  index = index + 1

print("\n---- LAST GEN ----")
print(str(cromossomes[min_index].getMultiplier()) + " * " + cromossomes[min_index].getExpression())
print("Score: " + str(cromossomes[min_index].getScore()))