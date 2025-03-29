def cancel_booking(self, flight_id, passenger_id):
    flight = None
    for f in self.flights:
        if f.flight_id == flight_id:
            flight = f
            break

    passenger = self.search_passenger(passenger_id)

    if flight and passenger and flight_id in passenger.booked_flights:
        passenger.booked_flights.remove(flight_id)
        flight.available_seats += 1
        refund = self.calculate_refund(datetime.now())
        self.save_data()
        return f"Cancellation successful. Refund: ₹{refund}."

    return "Invalid cancellation request."
