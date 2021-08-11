from queue import Queue
class bsf :

    def __init__(self,aj_list) :
        self.aj_list = aj_list
        self.visited = {}
        self.level = {}
        self.parent = {}
        self.bfs_traversal = []
        self.queue = Queue()
        print(f"adjestion list is : {self.aj_list}")
    def graph(self) :
        for node in self.aj_list.keys() :
            self.visited[node] = False
            self.parent[node] = None
            self.level[node] = -1
    def source(self) :
        s = "A"
        self.visited[s] = True
        self.level[s] = 0
        self.queue.put(s)
    def opration(self) :
        while not self.queue.empty() :
            u = self.queue.get()
            #print(u)
            self.bfs_traversal.append(u)
            for v in self.aj_list[u] :
                if not self.visited[v] :
                    self.visited[v] = True
                    self.parent[v] = u
                    self.level[v] = self.level[u] + 1
                    self.queue.put(v)

    def display(self) :
        print(f"visited nodes : {self.bfs_traversal}")
        d = self.level["A"]
        print(f"level of G is : {d}")

aj_list = {
  "A" : ["B", "D"],
  "B" : ["A", "C"],
  "C" : ["B"],
  "D" : ["A", "E", "F"],
  "E" : ["D", "F", "G"],
  "F" : ["D", "E", "H"],
  "G" : ["E", "H"],
  "H" : ["G", "F"]
}

obj = bsf(aj_list)
obj.graph()
obj.source()
obj.opration()
obj.display()