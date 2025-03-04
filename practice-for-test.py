class Cab:
    platform = "Uber"

    def __init__(self,cab_id,total_seats,rating):
        self.cab_id = cab_id
        self.total_seats = total_seats
        self.rating = rating

    def get_details(self):
        return f"Cab Id: {self.cab_id}, Total Seats: {self.total_seats}, Rating: {self.rating}"

    @classmethod
    def change_platform(cls, new_platform):
        cls.platform = new_platform

    @staticmethod
    def check_mini_suv(seats):
        if seats <= 4:
            return True
        else:
            return False
        
class Route:
    def __init__(self,pickup_venue,drop_venue):
        self.pickup_venue = pickup_venue
        self.drop_venue = drop_venue

    def get_route(self):
        return f"Pickup Venue: {self.pickup_venue}, Drop Venue: {self.drop_venue}"
    
class Pasanger:
    def __init__(self, cab, route):
        self.cab = cab
        self.route = route

    def get_cab_info(self):
        return f"Cab Details: {self.cab.get_details()} Route Details: {self.route.get_route()}"

cab1 = Cab("CAR125",5,4.5)
route1 = Route("Bangalore", "Mysore")
passenger1 = Pasanger(cab1, route1)

print(passenger1.get_cab_info())
print(Cab.check_mini_suv(cab1.total_seats))

Cab.change_platform("Ola")
print(cab1.get_details())
