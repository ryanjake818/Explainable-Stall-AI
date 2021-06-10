import random

import matplotlib.pyplot as plt
import pandas as pd

import FlightGeneration.dcd.FlightDataHelper as flightHelper

if __name__ == '__main__':
    # just random number of seconds between 1000 and 50000 to generate flight records every .1 second
    num_iterations = random.randint(1000, 50000) - 1

    # generate empty list for a flight
    flight_series = []
    # create intial flight with flight_id 1
    base_flight = flightHelper.create_flight(1)
    # add the first flight to the list
    flight_series.append(base_flight)
    for i in range(num_iterations):
        # always pull last flight record so we can use past data for calculations
        last_flight_record = flight_series[-1]
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
                                                                last_flight_record.cur_airspeed,
                                                                last_flight_record.angle_of_attack)
        if new_flight_record.cur_altitude <= 0:
            break
        # add new record to the list
        flight_series.append(new_flight_record)

    # convert list to dataframe
    df = pd.DataFrame([x.to_dict() for x in flight_series])

    # print dataframe
    print(df)
    df.to_excel("Stall_Data.xlsx")

    fig, axs = plt.subplots(7)
    axs[0].plot(df['cur_time'], df['cur_altitude'])
    axs[0].set_title('cur_time vs cur_altitude')
    axs[1].plot(df['cur_time'], df['cur_airspeed'])
    axs[1].set_title('cur_time vs cur_airspeed')
    axs[2].plot(df['cur_time'], df['vertical_speed'])
    axs[2].set_title('cur_time vs vertical_speed')
    axs[3].plot(df['cur_time'], df['angle_of_attack'])
    axs[3].set_title('cur_time vs angle_of_attack')
    axs[4].plot(df['cur_time'], df['flight_path_angle'])
    axs[4].set_title('cur_time vs flight_path_angle')
    axs[5].plot(df['cur_time'], df['pitch_angle'])
    axs[5].set_title('cur_time vs pitch_angle')
    axs[6].plot(df['cur_time'], df['roll'])
    axs[6].set_title('cur_time vs roll')
    plt.show()

    # just looking at first 10 records
    for i in range(10):
        print(flight_series[i].to_dict())
