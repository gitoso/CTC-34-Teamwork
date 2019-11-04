#!python
from math import sin, cos, sqrt, log, exp, isnan, isinf
import pandas
import csv
import random
import time
from grammar import Grammar
from genetic import Cromossome, fight

# Open .csv file and import it in a dictionary structure
#data = pandas.read_csv("csv-files/reduced.csv")
#data = pandas.read_csv("csv-files/training.csv")

with open('csv-files/training.csv', 'r') as f:
  data = list(csv.reader(f, delimiter=","))
data.pop(0)

for element in data:
  if element == []:
    data.remove(element)

# Variable names (hardcoded)
ID = 0
Cement = 1
Blasr = 2
FlyAsh = 3
Water = 4
Superplasticizer = 5
CoarseAggregate = 6
FineAggregate = 7
Age = 8
strenght = 9


# Genetic parameters
C_SIZE = 30
POPULATION = 1000 # Must be an even number
C_RANGE = 20
MIX_PROB = 0.8
MUT_PROB = 0.1
NUM_GENERATIONS = 30

# Initialize grammar
grammar = Grammar()
grammar.setVariables(['ID', 'Cement', 'Blasr', 'FlyAsh', 'Water', 'Superplasticizer', 'CoarseAggregate', 'FineAggregate', 'Age'])

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
  start = time.time()

  for C in cromossomes:
    if not C.isEvaluated():
      C.setExpression(grammar.cromossomeToExpression(C))

  # Evaluate cromossomes scores

  # Evaluate expression
  for C in cromossomes:
    mathErrorFlag = False
    avgScore = 0
    count = 0
    v = {'ID': 0, 'Cement': 0, 'Blasr': 0, 'FlyAsh': 0, 'Water': 0, 'Superplasticizer': 0, 'CoarseAggregate': 0, 'FineAggregate': 0, 'Age': 0}
    compiled = compile(C.getExpression(), '<string>', 'eval')

    if not C.isErroneous():
      for row in data:
        v['ID'] = float(data[count][ID])
        v['Cement'] = float(data[count][Cement])
        v['Blasr'] = float(data[count][Blasr])
        v['FlyAsh'] = float(data[count][FlyAsh])
        v['Water'] = float(data[count][Water])
        v['Superplasticizer'] = float(data[count][Superplasticizer])
        v['CoarseAggregate'] = float(data[count][CoarseAggregate])
        v['FineAggregate'] = float(data[count][FineAggregate])
        v['Age'] = float(data[count][Age])

        try:
          calculated = eval(compiled)
        except:
          mathErrorFlag = True
          calculated = 0
        score = (float(data[count][strenght]) - calculated) ** 2
        
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

  print(cromossomes[min_index].getExpression())
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

  for row in data:
    v['ID'] = float(data[count][ID])
    v['Cement'] = float(data[count][Cement])
    v['Blasr'] = float(data[count][Blasr])
    v['FlyAsh'] = float(data[count][FlyAsh])
    v['Water'] = float(data[count][Water])
    v['Superplasticizer'] = float(data[count][Superplasticizer])
    v['CoarseAggregate'] = float(data[count][CoarseAggregate])
    v['FineAggregate'] = float(data[count][FineAggregate])
    v['Age'] = float(data[count][Age])

    try:
      calculated = eval(C.getExpression())
    except:
      mathErrorFlag = True
      calculated = 0
    score = (float(data[count][strenght]) - calculated) ** 2
    
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
print(cromossomes[min_index].getExpression())
print("Score: " + str(cromossomes[min_index].getScore()))