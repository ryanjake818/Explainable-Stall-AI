import random

import pandas as pd

import FlightGeneration.dcd.FlightDataHelper as flightHelper


def create_flight_records(flight_id, writer):
    # just random number of seconds between 1000 and 50000 to generate flight records every .1 second
    num_iterations = random.randint(1000, 50000) - 1

    # generate empty list for a flight
    flight_series = []
    # create initial flight with flight_id 1
    base_flight = flightHelper.create_flight(flight_id)
    # add the first flight to the list
    flight_series.append(base_flight)
    for i in range(num_iterations):
        # always pull last flight record so we can use past data for calculations
        last_flight_record = flight_series[-1]
        last_two_seconds = flight_series[-19:]
        # create new record, this is using FlightDataHelper classes generate_flight_record method
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
                                                                last_two_seconds,
                                                                last_flight_record.cur_airspeed,
                                                                last_flight_record.angle_of_attack,
                                                                last_flight_record.sign_flag)
        if new_flight_record.cur_altitude <= 0:
            break
        # add new record to the list
        flight_series.append(new_flight_record)

    # convert list to dataframe
    df = pd.DataFrame([x.to_dict() for x in flight_series])

    # put df in excel

    df.to_excel(writer, sheet_name=f"sheet_data_{flight_id}")


if __name__ == '__main__':
    writer = pd.ExcelWriter('stall_data.xlsx', engine='xlsxwriter')
    for i in range(1):
        create_flight_records(i, writer)
    writer.save()
