#!python
from math import sin, cos, sqrt, log, exp, isnan, isinf
import csv
import random
import time
from grammar import Grammar
from genetic import Cromossome, fight, newCromossomeList, evaluateExpression, evaluateScore

from selection import tournament
from genetic_combination import combination
from mutation import mutation

# Open .csv file and import it in a dictionary structure
#data = pandas.read_csv("csv-files/reduced.csv")
#data = pandas.read_csv("csv-files/training.csv")

with open('csv-files/training.csv', 'r') as f:
  data = list(csv.reader(f, delimiter=","))
data.pop(0)

for element in data:
  if element == []:
    data.remove(element)

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
cromossomes = newCromossomeList(POPULATION, C_SIZE, C_RANGE)

for generation in range(NUM_GENERATIONS):
  message = "\n---- Generation: " + str(generation) + " ----"
  print(message)

  # Convert cromossomes to expressions
  for C in cromossomes:
    if not C.isEvaluated():
      C.setExpression(grammar.cromossomeToExpression(C))

  # Evaluate cromossomes scores

  # Evaluate expression
  for C in cromossomes:
    evaluateExpression(C, data)

  # Min score
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

  # Selection
  winners = tournament(cromossomes, POPULATION)

  # Genetic combination
  newGeneration = combination(cromossomes, C_SIZE, POPULATION, MIX_PROB)

  # Mutation
  mutation(newGeneration, MUT_PROB, C_SIZE, C_RANGE)

  cromossomes = newGeneration

# Last generation selection
for C in cromossomes:
    C.setExpression(grammar.cromossomeToExpression(C))

# Evaluate cromossomes scores
for C in cromossomes:
  evaluateScore(C, data)

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