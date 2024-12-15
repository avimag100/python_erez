import route_planner
from sort_strategy import QuickSortStrategy, MergeSortStrategy
from vehicle import Bus, Train, Tram


def main():
    planner = route_planner.RoutePlanner()
    menu = """
    1. Add vehicle
    2. Remove vehicle
    3. View vehicles
    4. Find optimal route
    5. Sort vehicles
    6. Exit
    """
    
    while True:
        print(menu)
        choice = input("Enter choice: ")

        if choice == "1":
            vehicle_type = input("Enter vehicle type (bus/train/tram): ")
            vehicle_id = input("Enter vehicle ID: ")
            capacity = int(input("Enter vehicle capacity: "))
            speed = int(input("Enter vehicle speed (km/h): "))
            
            if vehicle_type == "bus":
                route_number = input("Enter bus route number: ")
                vehicle = Bus(vehicle_id, capacity, speed, route_number)
            elif vehicle_type == "train":
                line_name = input("Enter train line name: ")
                num_cars = int(input("Enter number of cars: "))
                vehicle = Train(vehicle_id, capacity, speed, line_name, num_cars)
            elif vehicle_type == "tram":
                track_length = float(input("Enter tram track length (km): "))
                vehicle = Tram(vehicle_id, capacity, speed, track_length)
            else:
                print("Invalid vehicle type")
                continue

            planner.add_vehicle(vehicle)

        elif choice == "2":
            vehicle_id = input("Enter vehicle ID to remove: ")
            planner.remove_vehicle(vehicle_id)

        elif choice == "3":
            for vehicle in planner.vehicles:
                print(vehicle.get_details())

        elif choice == "4":
            start = input("Enter start point: ")
            end = input("Enter end point: ")
            algorithm = input("Enter algorithm (dijkstra/a_star): ")
            path = planner.find_optimal_route(start, end, algorithm)
            print("Optimal path:", path)

        elif choice == "5":
            sort_strategy = input("Enter sorting strategy (quick/merge): ")
            if sort_strategy == "quick":
                strategy = QuickSortStrategy()
            else:
                strategy = MergeSortStrategy()
            planner.sort_vehicles(strategy)
            print("Vehicles sorted.")

        elif choice == "6":
            break


if __name__ == "__main__":
    main()
