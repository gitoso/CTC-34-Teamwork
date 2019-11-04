import random

def fight(C1, C2):
  if C1.getScore() < C2.getScore():
    return C1
  else:
    return C2


class Cromossome():
  cromossomeList = []
  score = 999999999
  multiplier = 1
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