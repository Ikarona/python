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
        self.matrix = [['0' * len(self.my_graph_list)] for i in range(len(self.my_graph_list))]
        for x in range(len(gr)):
            matrix[gr[x][0],gr[x][1]] = gr[x][2]
