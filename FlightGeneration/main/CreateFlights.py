import random

import FlightGeneration.dcd.FlightDataHelper as flightHelper

if __name__ == '__main__':
    num_iterations = random.randint(1000, 50000) - 1

    flight_series = []
    base_flight = flightHelper.create_flight(1)
    flight_series.append(base_flight)
    for i in range(num_iterations):
        last_flight_record = flight_series[-1]
        new_flight_record = flightHelper.generate_flight_record(last_flight_record.flight_id,
                                                                last_flight_record.initial_alt,
                                                                last_flight_record.time_to_buffet,
                                                                last_flight_record.time_from_buffet_to_uncommanded_descent,
                                                                last_flight_record.magnitude_of_uncommanded_descent,
                                                                last_flight_record.time_from_buffet_to_uncommanded_roll,
                                                                last_flight_record.magnitude_of_uncommanded_roll,
                                                                last_flight_record.period_of_uncommanded_roll,
                                                                last_flight_record.initial_airspeed,
                                                                last_flight_record.time_from_buffet_to_uncommanded_descent_high,
                                                                last_flight_record.magnitude_of_uncommanded_descent_high,
                                                                last_flight_record.time_from_buffet_to_positive_angle_of_attack,
                                                                last_flight_record.max_angle_of_attack,
                                                                last_flight_record.rate_of_change_in_angle_of_attack,
                                                                last_flight_record.cur_time,
                                                                last_flight_record.cur_altitude,
                                                                last_flight_record.cur_airspeed,
                                                                last_flight_record.angle_of_attack)
        flight_series.append(new_flight_record)

    for i in range(10):
        print(flight_series[i].to_dict())
