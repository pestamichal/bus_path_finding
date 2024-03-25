import heapq
import time


class PriorityQueue:

    def __init__(self):
        self.list: list = []

    def empty(self):
        return not self.list

    def put(self, item, priority):
        heapq.heappush(self.list, (priority, item))

    def get(self):
        return heapq.heappop(self.list)[1]

def recreate_path(start, goal, path):
    path_info = []
    current_stop = goal
    end_stop = goal
    current_line = path[goal][1].line
    arrival = path[goal][1].arrival


    while current_stop != start:
        edge = path[current_stop][1]
        current_stop = path[current_stop][0]
        if edge.line != current_line or current_stop == start:
            path_info.append(
                f'Line: {current_line} dep: {current_stop} at '
                f'{edge.departure} arr: {end_stop} at {arrival}'
            )
            end_stop = current_stop
            arrival = edge.arrival
            current_line = edge.line

    path_info.reverse()
    for line in path_info:
        print(line)

def recreate_path2(start, goal, path):
    path_info = []
    current_stop = goal
    end_stop = goal
    last_line = path[goal][1].line
    arrival = path[goal][1].arrival
    last_departure = path[goal][1].departure
    while current_stop != start:
        edge = path[current_stop][1]
        current_stop = path[current_stop][0]
        if edge.line != last_line or current_stop == start:
            path_info.append(
                f'Line: {last_line} dep: {current_stop} at '
                f'{last_departure} arr: {end_stop} at {arrival}'
            )
            arrival = edge.arrival
            end_stop = edge.end_stop_name
        last_departure = edge.departure
        last_line = edge.line

    path_info.reverse()
    for line in path_info:
        print(line)


def dijkstra_time(graph, start, goal, start_time):
    q = PriorityQueue()
    q.put(start, 0)
    current_cost = dict()
    path = dict()
    current_cost[start] = 0
    path[start] = None

    t1 = time.time()

    while not q.empty():
        current_node = q.get()
        current_time = start_time + current_cost[current_node]
        if current_node == goal:
            recreate_path2(start, goal, path)
            print(f'Dijsktra time: {time.time() - t1}')
            return

        for node in graph.get_neighbors(current_node):
            edge = graph.get_fastest_connection(current_node, node, current_time)
            if edge is None:
                continue
            cost = current_cost[current_node] + (edge.arrival - current_time).seconds()
            next_node = edge.end_stop_name

            if next_node not in current_cost or cost < current_cost[next_node]:
                current_cost[next_node] = cost
                priority = cost
                q.put(next_node, priority)
                path[next_node] = (current_node, edge)
    return None


def astar_time(graph, start, goal, start_time):
    q = PriorityQueue()
    q.put(start, 0)
    current_cost = dict()
    path = dict()
    current_cost[start] = 0
    path[start] = None

    t1 = time.time()

    while not q.empty():
        current_node = q.get()
        current_time = start_time + current_cost[current_node]
        if current_node == goal:
            recreate_path2(start, goal, path)
            print(f'A* time: {time.time() - t1}')
            return

        for node in graph.get_neighbors(current_node):
            edge = graph.get_fastest_connection(current_node, node, current_time)
            if edge is None:
                continue
            cost = current_cost[current_node] + (edge.arrival - current_time).seconds()
            next_node = edge.end_stop_name

            if next_node not in current_cost or cost < current_cost[next_node]:
                current_cost[next_node] = cost
                priority = cost + time_heuristic((graph.nodes[next_node]), (graph.nodes[goal]))
                q.put(next_node, priority)
                path[next_node] = (current_node, edge)

    return None


def time_heuristic(current_node, goal):
    return (abs(float(current_node[0]) - float(goal[0])) + abs(float(current_node[1]) - float(goal[1]))) * 10000



def astar_transfers(graph, start, goal, start_time):
    q = PriorityQueue()
    q.put(start, 0)
    current_cost = dict()
    path = dict()
    current_cost[start] = 0
    path[start] = None

    t1 = time.time()

    while not q.empty():
        current_node = q.get()
        current_time = start_time + current_cost[current_node]
        if current_node == goal:
            recreate_path2(start, goal, path)
            print(f'A* time: {time.time() - t1}')
            return

        for node in graph.get_neighbors(current_node):
            edge = graph.get_fastest_connection(current_node, node, current_time)
            if edge is None:
                continue
            cost = current_cost[current_node] + (edge.arrival - current_time).seconds()
            next_node = edge.end_stop_name

            if next_node not in current_cost or cost < current_cost[next_node]:
                current_cost[next_node] = cost
                priority = cost + time_heuristic((graph.nodes[next_node]), (graph.nodes[goal]))
                q.put(next_node, priority)
                path[next_node] = (current_node, edge)

    return None


