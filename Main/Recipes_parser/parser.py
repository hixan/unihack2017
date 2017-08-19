def parser(values):
  results = []
  results2 = []
  results3 = []
  results4 = []
  name = ""
  with open('../../Tests/basic_test_data.txt') as inputfile:
    for line in inputfile:
      results.append(line.strip().strip(","))
  for line in results:
    if(len(line) > 0):
      if((line[0] == '"')and(line.find(":")==-1)):
        results2.append(line)
      if(line.find("title") != -1):
        if(len(results2) != 0):
          results4 = []
          results4.append(name)
          results4.append(results2)
          results3.append(results4)
          results2 = []
        name = line
  for line in results3:
    for item in line[1]:
      for value in values:
        if value not in item:
          results2.append(item)
      print(line[0])
  print(values)
parser('milk')
