import csv

file_path = 'connection_graph.csv'
graph = {}

# Main node representation: stop_name, location (x, y)
# Edges representation: (stop_name, location), line, departure, arrival (line/arrival criteria, departure => can we make it)

class Edge:
    def __init__(self, start_stop_name, end_stop_name, line, departure_from_start, arrival_at_end):
        self.start_stop_name = start_stop_name
        self.end_stop_name = end_stop_name
        self.line = line
        self.departure_from_start = departure_from_start
        self.arrival_at_end = arrival_at_end

def create_graph_from_a_file():
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            start_stop_name = create_vertex_name(['start_stop'],row['start_stop_lat'], row['start_stop_lon'])
            end_stop_name = create_vertex_name(row['end_stop'], row['end_stop_lat'], row['end_stop_lon'])
            add_vertex(start_stop_name)
            add_vertex(end_stop_name)
            add_edge()

def create_vertex_name(stop_name, x, y):
    return stop_name + ' (' + str(x) + ', ' + str(y) + ')'

def add_vertex(stop_name):
    if stop_name not in graph:
        graph[stop_name] = []

def add_edge(start_stop_name, end_stop_name, line, departure_from_start, arrival_at_end):
    if start_stop_name in graph and end_stop_name in graph:
        edge = Edge(start_stop_name, end_stop_name, line, departure_from_start, arrival_at_end)

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')


