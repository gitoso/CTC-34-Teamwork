import csv
from math import sin, cos, sqrt, log, exp, isnan, isinf

expression = "sqrt(sqrt(v['Age']*sqrt(v['Cement'])))"
compiled = compile(expression, '<string>', 'eval')

csvHeaders = []

with open('csv-files/testing.csv', 'r') as f:
  data = list(csv.reader(f, delimiter=","))
  csvHeaders = data[0]
data.pop(0)

for element in data:
  if element == []:
    data.remove(element)

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

v = {'ID': 0, 'Cement': 0, 'Blasr': 0, 'FlyAsh': 0, 'Water': 0, 'Superplasticizer': 0, 'CoarseAggregate': 0, 'FineAggregate': 0, 'Age': 0}

result = []

count = 0
for row in data:
  print(row)
  v['ID'] = float(data[count][ID])
  v['Cement'] = float(data[count][Cement])
  v['Blasr'] = float(data[count][Blasr])
  v['FlyAsh'] = float(data[count][FlyAsh])
  v['Water'] = float(data[count][Water])
  v['Superplasticizer'] = float(data[count][Superplasticizer])
  v['CoarseAggregate'] = float(data[count][CoarseAggregate])
  v['FineAggregate'] = float(data[count][FineAggregate])
  v['Age'] = float(data[count][Age])

  id = float(data[count][ID])
  calculated = eval(compiled)

  count = count + 1
  result.append((id, calculated))

with open('csv-files/result.csv', 'w') as csvfile:
  newData = csv.writer(csvfile, delimiter=',')
  newData.writerow(['ID','strength'])
  for element in result:
    newData.writerow([int(element[0]), element[1]])

