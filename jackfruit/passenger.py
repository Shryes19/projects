class Passenger:
    def __init__(self, passenger_id, name, contact_details, booked_flights=None):
        self.passenger_id = passenger_id
        self.name = name
        self.contact_details = contact_details
        self.booked_flights = booked_flights if booked_flights else []

    def add_flight(self, flight_id):
        if flight_id not in self.booked_flights:
            self.booked_flights.append(flight_id)

    def remove_flight(self, flight_id):
        if flight_id in self.booked_flights:
            self.booked_flights.remove(flight_id)

    def to_csv(self):
        return [self.passenger_id, self.name, self.contact_details, ','.join(self.booked_flights)]