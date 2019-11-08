import random
from math import isnan

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

def fight(C1, C2):
  if C1.getScore() < C2.getScore():
    return C1
  else:
    return C2

def newCromossomeList(POPULATION, C_SIZE, C_RANGE):
  cromossomes = []
  for n in range(POPULATION):
    C = Cromossome()
    C.setRandomList(C_SIZE, C_RANGE)
    cromossomes.append(C)
  
  return cromossomes

def evaluateExpression(C, data):
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

def evaluateScore(C, data):
  mathErrorFlag = False
  avgScore = 0
  count = 0
  v = {'ID': 0, 'Cement': 0, 'Blasr': 0, 'FlyAsh': 0, 'Water': 0, 'Superplasticizer': 0, 'CoarseAggregate': 0, 'FineAggregate': 0, 'Age': 0}

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

class Cromossome():
  cromossomeList = []
  score = 999999999
  expression = ''
  evaluated = False
  mathError = False

  def setRandomList(self, cromossomeSize, cromossomeRange):
    randomList = [random.randint(0, cromossomeRange) for x in range(0, cromossomeSize)]
    self.setCromossomeList(randomList)

  def setExpression(self, expression):
    self.expression = expression
    self.evaluated = True

  def setScore(self, score):
    self.score = score

  def setMultiplier(self, multiplier):
    self.multiplier = multiplier

  def setEvaluated(self):
    self.evaluated = True

  def setCromossomeList(self, cromossomeList):
    self.cromossomeList = cromossomeList

  def changeCromossomeAtPosition(self, position, newValue):
    self.cromossomeList[position] = newValue

  def setErroneous(self):
    self.mathError = True

  def getList(self):
    return self.cromossomeList

  def getScore(self):
    return self.score

  def getMultiplier(self):
    return self.multiplier

  def getExpression(self):
    return self.expression

  def isEvaluated(self):
    return self.evaluated

  def isErroneous(self):
    return self.mathError