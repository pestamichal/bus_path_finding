import csv
from graph import Graph
import pickle


file_path = 'connection_graph.csv'
graph = Graph()

def create_vertex_name(stop_name, x, y):
    return stop_name + ' (' + str(x) + ', ' + str(y) + ')'

def create_graph_from_a_file():
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            start_stop_name = create_vertex_name(row['start_stop'],row['start_stop_lat'], row['start_stop_lon'])
            end_stop_name = create_vertex_name(row['end_stop'], row['end_stop_lat'], row['end_stop_lon'])
            graph.add_vertex(start_stop_name, row['start_stop_lat'], row['start_stop_lon'])
            graph.add_vertex(end_stop_name, row['end_stop_lat'], row['end_stop_lon'])
            graph.add_edge(start_stop_name, end_stop_name, row['line'], row['departure_time'], row['arrival_time'])

    with open('graph_instance.pkl', 'wb') as f:
        pickle.dump(graph, f)

def restore_graph():
    with open('graph_instance.pkl', 'rb') as f:
        graph = pickle.load(f)
    graph.print_graph()
    # print(graph.get_neighbors('Miękinia - Urząd Gminy (51.19386776, 16.73806496)'))
    # print(graph.get_fastest_connection('Miękinia - Urząd Gminy (51.19386776, 16.73806496)', 'Klęka (51.20861669, 16.7499646)', '12:00:00'))


if __name__ == '__main__':
    # create_graph_from_a_file()
    restore_graph()


