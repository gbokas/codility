def InitializeConnection(numberObject):
  connections = []
  for i in range(numberObject):
    connections.append(i)
  return connections

def FindConnection(firstId, secondId, connections):
  return connections[firstId] == connections[secondId]

def UnionObjects(objectFirst, objectSecond, connections):
  tmpFirst = connections[objectFirst]
  tmpSecond = connections[objectSecond]
  connections[objectSecond] = connections[objectFirst]
  for i in range(len(connections)):
    if tmpSecond == connections[i]: connections[i] == connections[objectFirst]
  return connections
  

connections = InitializeConnection(40)
first = [2, 5, 15, 15, 17, 20, 34, 21, 36, 12, 32, 11]
second = [5, 1, 8, 12, 13, 21, 31, 1, 28, 32, 11, 12]
for i, j in zip(first, second):
  connections = UnionObjects(i, j, connections)

print(FindConnection(8, 32, connections))
