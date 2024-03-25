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
    return len(path_info) - 1

def dijkstra_time(graph, start, goal, start_time):
    q = PriorityQueue()
    q.put(start, 0)
    current_cost = {start: 0}
    path = {start: None}

    t1 = time.time()

    while not q.empty():
        current_node = q.get()
        current_time = start_time + current_cost[current_node]
        if current_node == goal:
            transfers = recreate_path2(start, goal, path)
            print(f'Dijsktra calculation time: {time.time() - t1}')
            print(f'Dijkstra total travel time: {(path[goal][1].arrival - start_time).seconds()}')
            print(f'Dijkstra total transfers: {transfers}')
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
    print('Path not found')
    return None


def astar_time(graph, start, goal, start_time):
    q = PriorityQueue()
    q.put(start, 0)
    current_cost = {start: 0}
    path = {start: None}

    t1 = time.time()

    while not q.empty():
        current_node = q.get()
        current_time = start_time + current_cost[current_node]
        if current_node == goal:
            transfers = recreate_path2(start, goal, path)
            print(f'A* calculation time: {time.time() - t1}')
            print(f'A* total travel time: {(path[goal][1].arrival - start_time).seconds()}')
            print(f'A* total transfers: {transfers}')
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
    print('Path not found')
    return None


def time_heuristic(current_node, goal):
    return (abs(float(current_node[0]) - float(goal[0])) + abs(float(current_node[1]) - float(goal[1]))) * 10000



def astar_transfers(graph, start, goal, start_time):
    q = PriorityQueue()
    q.put(start, 0)
    current_cost = {start: 0}
    path = {start: None}
    node_time = {start: 0}

    goal_lines = []
    for edge in graph.graph[goal]:
        goal_lines.append(edge.line)

    t1 = time.time()

    while not q.empty():
        current_node = q.get()
        current_time = start_time + node_time[current_node]
        if current_node == goal:
            transfers = recreate_path2(start, goal, path)
            print(f'A* transfers calculation time: {time.time() - t1}')
            print(f'A* transfers total travel time: {(path[goal][1].arrival - start_time).seconds()}')
            print(f'A* total transfers: {transfers}')
            return

        for edge in graph.get_connections_after_time(current_node, current_time):

            next_node = edge.end_stop_name

            new_time = node_time[current_node] + (edge.arrival - current_time).seconds()
            cost = current_cost[current_node] + (0 if path[current_node] is None or edge.line == path[current_node][1].line else 2) + new_time / 3600

            if next_node not in current_cost or cost < current_cost[next_node]:
                current_cost[next_node] = cost
                node_time[next_node] = new_time
                priority = cost + transfer_heuristic(edge.line, goal_lines)
                q.put(next_node, priority)
                path[next_node] = (current_node, edge)
    print('Path not found')
    return None


def transfer_heuristic(current_line, goal_lines):
    return 0 if current_line in goal_lines else 1

