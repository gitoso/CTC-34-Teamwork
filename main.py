#!/usr/bin/python
import pandas
import math
from grammar import Grammar

# Open .csv file and import it in a dictionary structure
data = pandas.read_csv("csv-files/training.csv")

# Parameters


# Initialize grammar
grammar = Grammar()
#grammar.setVariables(['x', 'y'])
grammar.setVariables(data.keys()[0:-1])


# Initial cromossomes
cromossomes = []
cromossomes.append([4, 15, 75, 8, 41, 12])
cromossomes.append([6, 10, 255, 7, 50, 35])
cromossomes.append([9, 40, 7, 43, 2, 11])
cromossomes.append([20, 5, 200, 5, 67, 23])

# Convert cromossomes to expressions
expressions = []
for cromossome in cromossomes:
  expressions.append(grammar.cromossomeToExpression(cromossome))


# Evaluate cromossomes scores
cromossomesScores = []

for expression in expressions:
  avgScore = 0
  count = 0

  for row in data.ID:
    ID = data.ID[row - 1]
    Cement = data.Cement[row - 1]
    Blasr = data.Blasr[row - 1]
    FlyAsh = data.FlyAsh[row - 1]
    Water = data.Water[row - 1]
    Superplasticizer = data.Superplasticizer[row - 1]
    CoarseAggregate = data.CoarseAggregate[row - 1]
    FineAggregate = data.FineAggregate[row - 1]
    Age = data.Age[row - 1]

    calculated = eval(expression)
    score = (data.strength[row - 1] - calculated) ** 2
    
    avgScore = avgScore + score
    count = count + 1
  
  avgScore = avgScore / count
  if math.isnan(avgScore):
    avgScore = 100000
  cromossomesScores.append(avgScore)

print(cromossomesScores)



# Evaluate expressions
# x = 5
# y = 1
# for expression in expressions:
#   eval(expression)

# Tournament


# Genetic combination


# Mutation
