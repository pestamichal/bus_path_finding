import heapq


class PriorityQueue:

    def __init__(self):
        self.list: list = []

    def empty(self):
        return not self.list

    def put(self, item, priority):
        heapq.heappush(self.list, (priority, item))

    def get(self):
        return heapq.heappop(self.list)

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




def dijkstra_time(graph, start, goal, start_time):
    q = PriorityQueue()
    q.put(start, 0)
    costs = {start: 0}
    path = {start: None}

    while not q.empty():
        current_time, current_node = q.get()
        current_time = start_time + costs[current_node]

        if current_node == goal:
            recreate_path(start, goal, path)
            return

        for node in graph.get_neighbors(current_node):
            edge = graph.get_fastest_connection(current_node, node, current_time)
            cost = costs[current_node] + (edge.arrival - current_time).seconds()

            if node not in costs or cost < costs[node]:
                costs[node] = cost
                q.put(node, cost)
                path[node] = (current_node, edge)

    return