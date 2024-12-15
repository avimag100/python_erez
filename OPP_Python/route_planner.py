from algorithm import dijkstra, a_star
from sort_strategy import QuickSortStrategy, MergeSortStrategy


class RoutePlanner:
    def __init__(self):
        self.vehicles = []
        self.routes = {}

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle_id):
        self.vehicles = [v for v in self.vehicles if v.vehicle_id != vehicle_id]

    def find_optimal_route(self, start, end, algorithm):
        graph = self.routes  # Assume graph is stored in self.routes
        if algorithm == "dijkstra":
            return dijkstra(graph, start, end)
        elif algorithm == "a_star":
            return a_star(graph, start, end, heuristic=lambda x, y: 0)  # Example heuristic
        return None

    def sort_vehicles(self, strategy):
        self.vehicles = strategy.sort(self.vehicles)
