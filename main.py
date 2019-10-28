#!/usr/bin/python
import pandas
from grammar import Grammar

# Open .csv file and import it in a dictionary structure
#training = pandas.read_csv("csv-files/training.csv")

# Parameters


# Initialize grammar
grammar = Grammar()
grammar.setVariables(['x', 'y'])
#grammar.setVariables(training.keys());


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

# Evaluate expressions
x = 5
y = 1
for expression in expressions:
  eval(expression)

# Tournament


# Genetic combination


# Mutation
