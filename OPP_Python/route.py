class Route:
    def __init__(self, start_point, end_point, distance):
        self.start_point = start_point
        self.end_point = end_point
        self.distance = distance

    def get_route_info(self):
        return f"Route from {self.start_point} to {self.end_point}, Distance: {self.distance} km"
