'''
using copy-pasted alg of Dijkstra
'''
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

    def Dijkstra(self, START, NUMB):
        valid = [True]*NUMB
        weight = [1000000]*NUMB
        weight[START - 1] = 0
        for i in range(NUMB):
            MIN_WEIGHT = 1000001
            ID_MIN_WEIGHT = -1
            for i in range(len(weight)):
                if valid[i] and weight[i] < MIN_WEIGHT:
                    MIN_WEIGHT = weight[i]
                    ID_MIN_WEIGHT = i
            for i in range(len(self.my_graph_list)):
                if weight[ID_MIN_WEIGHT] + self.matrix[ID_MIN_WEIGHT][i] < weight[i]:
                    weight[i] = weight[ID_MIN_WEIGHT] + self.matrix[ID_MIN_WEIGHT][i]
            valid[ID_MIN_WEIGHT] = False
        weight.sort(reverse = True)
        if weight[0] > 10000:
            print(-1)
        else:
            print(weight[0])

TIMES = eval(input("times = "))
NUM = eval(input("N = "))
XXX = eval(input("X = "))
GRA = Graph(TIMES)
GRA.Dijkstra(XXX, NUM)
