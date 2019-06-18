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



  def get_ancestors(self, people, target):
    pass



  def bft(self, start_vertex, target_vertex):
    pass