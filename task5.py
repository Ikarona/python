class Graph:
    def __init__(self, gr):
        self.my_graph_list = []
        for x in range(len(gr)):
            while len(self.my_graph_list) < gr[x][0]:
                self.my_graph_list.append([])
            while len(self.my_graph_list) < gr[x][1]:
                self.my_graph_list.append([])
            self.my_graph_list[gr[x][0] - 1].append(gr[x][1])
            self.my_graph_list[gr[x][1] - 1].append(gr[x][0])
        self.matrix = [[1000000 for i in range(len(self.my_graph_list))] for i in range(len(self.my_graph_list))]
        for x in range(len(gr)):
            self.matrix[gr[x][0] - 1][gr[x][1] - 1] = gr[x][2]
            self.matrix[gr[x][1] - 1][gr[x][0] - 1] = gr[x][2]

    def Dijkstra(self, S, N):
        valid = [True]*N
        weight = [1000000]*N
        weight[S] = 0
        for i in range(N):
            min_weight = 1000001
            ID_min_weight = -1
            for i in range(len(weight)):
                if valid[i] and weight[i] < min_weight:
                    min_weight = weight[i]
                    ID_min_weight = i
            for i in range(len(self.my_graph_list)):
                if weight[ID_min_weight] + self.matrix[ID_min_weight][i] < weight[i]:
                    weight[i] = weight[ID_min_weight] + self.matrix[ID_min_weight][i]
            valid[ID_min_weight] = False
        weight.sort(reverse = True)
        if weight[0] > 10000:
            print(-1)
        else:
            print(weight[0])

times = eval(input("times = "))
N = eval(input("N = "))
X = eval(input("X = "))
n = Graph(times)
n.Dijkstra(X, N)