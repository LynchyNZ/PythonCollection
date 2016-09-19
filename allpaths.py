""" Calculates all paths from one node to another given a list of paths
E.g. 
# triangle graph (note: must add an extra ' " ' to both ' "" ' below.)
graph_str = ""
U 3
0 1
1 2
2 0
""
print(sorted(allpaths(Graph(graph_str), 0, 2))) -> [[0, 1, 2], [0, 2]]

Written by Daniel Lynch - 06/04/2015
"""

class Graph:
    def __init__(self, graph_string):
        self.graph_string = []
        for i in graph_string.splitlines():
            self.graph_string.append(i.split())

        def check_directed(self, graph_string):
            if self.graph_string[0][0] == "D":
                return True
            else:
                return False

        def check_weighted(self, graph_string):
            if self.graph_string[0][1] == "W":
                return True
            else:
                return False

        self.directed = check_directed(self, graph_string)
        self.weighted = check_weighted(self, self.graph_string)

        self.num = int(self.graph_string[0][1])

        self.adjacency_list = [[] for i in range(self.num)]
        self.graph_string.pop(0)
        if self.weighted:
            if self.directed:
                for i in self.graph_string:
                    self.adjacency_list[int(i[0])].append((int(i[1]), int(i[2])))
            else:
                for i in self.graph_string:
                    self.adjacency_list[int(i[0])].append((int(i[1]), int(i[2])))
                    self.adjacency_list[int(i[0])].append((int(i[0]), int(i[2])))
        else:
            if self.directed == True:
                for i in self.graph_string:
                    self.adjacency_list[int(i[0])].append((int(i[1]), None))
            else:
                for i in self.graph_string:
                    self.adjacency_list[int(i[0])].append((int(i[1]), None))
                    self.adjacency_list[int(i[1])].append((int(i[0]), None))              

def allpaths(graph, source, destination):
    paths = []
    success_paths = []
    for i in graph.adjacency_list[source]:
        paths.append([source, i[0]])
    while len(paths[0]) < len(graph.adjacency_list):
        new_paths = []
        for path in paths:
            end = path[-1]
            if end != destination and graph.adjacency_list[end] != []:
                for i in graph.adjacency_list[end]:
                        new_paths.append(path + [i[0]])
            else:
                if path[-1] == destination:
                    success_paths.append(path)
        paths = new_paths
    for i in new_paths:
        if i[-1] == destination:
            success_paths.append(i)
    final_paths = []
    for i in success_paths:
        if sorted(list(set(i))) == sorted(i):
            final_paths.append(i)
        
    return final_paths
    

# triangle graph
graph_str = """\
U 3
0 1
1 2
2 0
"""

print(sorted(allpaths(Graph(graph_str), 0, 2)))