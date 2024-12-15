from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, vehicle_id, capacity, speed):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.speed = speed

    @abstractmethod
    def get_details(self):
        return self.vehicle_id, self.capacity , self.speed

    def calculate_travel_time(self, distance):
        if self.speed == 0:
            return f'you will not get to your destanation because {self.speed} is your speed'  # Handle case where speed is 0 to avoid division by zero
        return distance / self.speed * 60  # Time in minutes

class Bus(Vehicle):
    def __init__(self, vehicle_id, capacity, speed, route_number):
        super().__init__(vehicle_id, capacity, speed)
        self.route_number = route_number

    def get_details(self):
        return f"Bus ID: {self.vehicle_id}, Capacity: {self.capacity}, Speed: {self.speed} km/h, Route: {self.route_number}"

class Train(Vehicle):
    def __init__(self, vehicle_id, capacity, speed, line_name, num_cars):
        super().__init__(vehicle_id, capacity, speed)
        self.line_name = line_name
        self.num_cars = num_cars

    def get_details(self):
        return f"Train ID: {self.vehicle_id}, Capacity: {self.capacity}, Speed: {self.speed} km/h, Line: {self.line_name}, Cars: {self.num_cars}"

class Tram(Vehicle):
    def __init__(self, vehicle_id, capacity, speed, track_length):
        super().__init__(vehicle_id, capacity, speed)
        self.track_length = track_length

    def get_details(self):
        return f"Tram ID: {self.vehicle_id}, Capacity: {self.capacity}, Speed: {self.speed} km/h, Track length: {self.track_length} km"
