#!python
from math import sin, cos, sqrt, isnan
import pandas
from grammar import Grammar

# Open .csv file and import it in a dictionary structure
#data = pandas.read_csv("csv-files/reduced.csv")
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
      calculated = eval(expression)
    except:
      mathErrorFlag = True
      calculated = 0
    score = (data.strength[count] - calculated) ** 2
    
    avgScore = avgScore + score
    count = count + 1
  
  avgScore = avgScore / count
  if isnan(avgScore) or mathErrorFlag:
    avgScore = 999999999
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
