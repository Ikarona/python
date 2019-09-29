from collections import deque
class Graph:
    def __init__(self, gr):
        self.my_graph_list = []
        for x in range(len(gr)):
            while len(self.my_graph_list) <= gr[x][0]:
                self.my_graph_list.append([])
            while len(self.my_graph_list) <= gr[x][1]:
                self.my_graph_list.append([])
            self.my_graph_list[gr[x][0]].append(gr[x][1])
            self.my_graph_list[gr[x][1]].append(gr[x][0])

    def help(self):
        self.vertex = []
        for i in range(0, len(self.my_graph_list)):
            if self.my_graph_list[i] not in self.vertex:
                self.vertex.append(self.my_graph_list[i][0])
        self.visited = [False] * len(self.vertex)
        self.depth = [-1] * len(self.vertex)

    def dfs(self, current):
        self.visited[current] = True
        print(current)
        for x in self.my_graph_list[current]:
            if not self.visited[x]:
                self.dfs(x)

    def bfs(self, current):
        self.depth[current] = 0
        q = deque()
        q.append(current)
        while q:
            current = q.popleft()
            print(current)
            for x in self.my_graph_list[current]:
                if self.depth[x] == -1:
                    q.append(x)
                    self.depth[x] = self.depth[current] + 1

gra=[[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
n = Graph(gra)

n.help()
print('dfs')
n.dfs(0)
print('bfs')
n.bfs(0)