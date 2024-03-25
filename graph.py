import matplotlib.pyplot as plt
from my_time import BusTime


class Edge:
    def __init__(self, end_stop_name, line, departure, arrival):
        self.end_stop_name = end_stop_name
        self.line = line
        self.departure = BusTime(departure)
        self.arrival = BusTime(arrival)

    def __str__(self):
        return f' --> {self.end_stop_name} by {self.line}, dep: {self.departure} arr: {self.arrival}'

    def __eq__(self, other):
        return self.end_stop_name == other.end_stop_name and self.line == other.line and self.departure == other.departure and self.arrival == other.arrival

class Graph:
    def __init__(self):
        self.graph = {}
        self.nodes = {}

    def add_vertex(self, stop_name, x, y):
        if stop_name not in self.graph:
            self.graph[stop_name] = []
            self.nodes[stop_name] = (x, y)
    def add_edge(self, start_stop_name, end_stop_name, line, departure, arrival):
        if start_stop_name in self.graph and end_stop_name in self.graph:
            edge = Edge(end_stop_name, line, departure, arrival)
            # if edge not in self.graph[start_stop_name]:
            self.graph[start_stop_name].append(edge)

    def get_connections_after_time(self, stop, time):
        result = []
        for edge in self.graph[stop]:
            if edge.departure >= time:
                result.append(edge)
        return sorted(result, key=lambda x: x.arrival)

    def get_neighbors(self, stop):
        result = set()
        for edge in self.graph[stop]:
            result.add(edge.end_stop_name)
        return result

    def get_fastest_connection(self, start_stop, end_stop, time):
        result = []
        for edge in self.graph[start_stop]:
            if edge.departure >= time and edge.end_stop_name == end_stop:
                result.append(edge)
        if len(result) == 0:
            return None
        return sorted(result, key=lambda x: x.arrival)[0]

    def print_graph(self):
        for node in self.graph:
            print(f'Node: {node}')
            for edge in self.graph[node]:
                print(edge)
    def print_nodes(self):
        for node in self.nodes:
            print(node)

    def get_random_node(self):
        pass

    def plot_nodes(self):
        x_vals = []
        y_vals = []
        for node in self.nodes:
            x_vals.append(float(self.nodes[node][0]))
            y_vals.append(float(self.nodes[node][1]))

        plt.scatter(x_vals, y_vals)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.show()