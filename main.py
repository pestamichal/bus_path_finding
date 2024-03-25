import csv
import pickle
import random

from algorithms import *
from graph import Graph
from my_time import BusTime

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
        return pickle.load(f)
    # graph.print_nodes()
    # print(graph.get_neighbors('Miękinia - Urząd Gminy (51.19386776, 16.73806496)'))
    # print(graph.get_fastest_connection('Miękinia - Urząd Gminy (51.19386776, 16.73806496)', 'Klęka (51.20861669, 16.7499646)', '12:00:00'))

def get_random_nodes(n):
    start_nodes = []
    end_nodes = []
    start_times = []
    for i in range(n):
        start_nodes.append(random.choice(list(graph.nodes.keys())))
        end_nodes.append(random.choice(list(graph.nodes.keys())))
        start_times.append(BusTime(h=random.randint(1, 22), m=random.randint(0, 59), s=random.randint(0, 59)))
    return start_nodes, end_nodes, start_times

def get_example_nodes():
    return \
        ['Strzegomska (krzyżówka) (51.112407, 16.960639)', 'Hutmen (51.09602766, 16.98631833)', 'RUBCZAKA (Stacja kolejowa) (51.14330576, 16.86637818)', 'Polkowicka (51.15526292, 16.87306982)', 'Dzielna (51.13863431, 16.97689014)', 'Żmudzka (51.145381, 17.141698)', 'SĘPOLNO (51.11377011, 17.10379057)', 'Jasińskiej (51.12098931, 16.87663189)', 'Brodzka (51.15816026, 16.9223663)', 'MUCHOBÓR MAŁY (Stacja kolejowa) (51.11257866, 16.9706042)', 'Stępin (51.20848301, 17.28088818)', 'Mokronos Dolny - Stawowa/Szczęśliwa (51.07132146, 16.93312583)', 'Karwińska (51.08204577, 17.0769832)'], \
        ['Wiaduktowa (51.07545298, 17.07609286)', 'Weigla (Szpital) (51.07644889, 17.01767649)', 'Gałczyńskiego (51.05505442, 17.03221101)', 'Dworska (51.14360635, 16.95344812)', 'Zalewowa (51.09049584, 17.13507911)', 'Lutynia I (51.135712, 16.771781)', 'Stanisławowska (W.K. Formaty) (51.09694613, 16.94689792)', 'Zielińskiego (51.098522, 17.02050515)', 'ROD Zgoda (51.06605814, 17.05995315)', 'Chińska (51.06088513, 17.08175746)', 'Ferma - stadnina koni (51.1180276, 16.8253587)', 'Psie Pole (Rondo Lotników Polskich) (51.14780568, 17.1149333)', 'DWORZEC AUTOBUSOWY (51.09746415, 17.03277662)'], \
        ['20:43:41', '10:48:57', '15:06:51', '19:45:57', '07:18:15', '15:45:00', '19:19:33', '10:44:59', '03:25:22', '14:16:09', '09:55:21', '06:08:50', '05:38:22']


if __name__ == '__main__':


    # time = BusTime(time_str='16:58:00')

    # dijkstra_time(graph, 'Wyszyńskiego (51.12232447, 17.05196291)', 'Jedności Narodowej (51.12102, 17.04326)', time)
    # astar_time(graph, 'Babimojska (51.114068, 16.977603)', 'Biegasa (51.099809, 17.086666)', time)
    # astar_transfers(graph, 'Babimojska (51.114068, 16.977603)', 'Biegasa (51.099809, 17.086666)', time)

    graph = restore_graph()
    #n = 3
    starting_nodes, end_nodes, times = get_example_nodes()
    n = len(starting_nodes)
        #get_random_nodes(n)

    for i in range(n):
        print(f'{starting_nodes[i]} ==> {end_nodes[i]} at: {times[i]}')
        print()
        dijkstra_time(graph, starting_nodes[i], end_nodes[i], BusTime(time_str=times[i]))
        print()
        astar_time(graph, starting_nodes[i], end_nodes[i], BusTime(time_str=times[i]))
        print()
        astar_transfers(graph, starting_nodes[i], end_nodes[i], BusTime(time_str=times[i]))
        print('=====================')

    #
    # while True:
    #     print('Select an action:')
    #     print('[*] Create new graph - 1')
    #     print('[*] Restore existing graph - 2')
    #     option = input()
    #     if int(option) == 1:
    #         create_graph_from_a_file()
    #         break
    #     elif int(option) == 2:
    #         print('Restoring graph from the local file...')
    #         graph = restore_graph()
    #         break
    #
    # print('Graph restored successfully!')
    # while True:
    #     start_stop = input('Departure stop: ')
    #     end_stop = input('Destination: ')
    #     print('Choose criteria: ')
    #     print('[*] Time criteria - t')
    #     print('[*] Transfers criteria - p')
    #     criteria = input()
    #     start_time = input('Departure time: ')
    #     if str(criteria) == 't':
    #         try:
    #             astar_time(graph, start_stop, end_stop, BusTime(time_str=start_time))
    #         except:
    #             print('An error occured')
    #     elif str(criteria) == 'p':
    #         try:
    #             astar_transfers(graph, start_stop, end_stop, BusTime(time_str=start_time))
    #         except:
    #             print('An error occured')
    #
    #     print('Exit program? [Y/n]')
    #     exit_program = input()
    #     if exit_program == '' or exit_program == 'y' or exit_program == 'Y':
    #         print('Exiting...')
    #         break






