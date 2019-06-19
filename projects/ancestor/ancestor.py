#  1. Translate the problem
#  2. Build your graph
#  3. Traverse your graph

class Queue():
  def __init__(self):
    self.queue = []
  def enqueue(self, value):
    self.queue.append(value)
  def dequeue(self):
    if self.size() > 0:
      return self.queue.pop(0)
    else:
      return None
  def size(self):
    return len(self.queue)

class Graph:
  def __init__(self):
    self.vertices = {}
  def add_vertex(self, vertex):
    self.vertices[vertex] = set()
  def add_edge(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
    else:
      raise IndexError('ERROR: That vertex does not exist.')

def earliest_ancestor(ancestors, starting_vertex):
  # Configure Graph
  graph = Graph()
  # Add vertices
  for i in range(1, 12):
    graph.add_vertex(i)
  # Reverse edges
  for anc in ancestors:
    graph.add_edge(anc[1], anc[0])
  # Implement BFS
  earliest_ancestor = -1
  longest_path = 1
  q = Queue()
  q.enqueue([starting_vertex])
  while q.size() > 0:
    path = q.dequeue()
    v = path[-1]
    if (len(path) == longest_path and v < earliest_ancestor) or (len(path) > longest_path):
      longest_path = len(path)
      earliest_ancestor = v
    for neighbor in graph.vertices[v]:
      path_copy = list(path)
      path_copy.append(neighbor)
      q.enqueue(path_copy)

  return earliest_ancestor

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))
