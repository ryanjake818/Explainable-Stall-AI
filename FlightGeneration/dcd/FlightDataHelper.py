import random

import numpy as np

from dcd.FlightData import FlightData


# first initial flight creation, lot of randomness to set the records
def create_flight(flight_id):
    initial_alt = random.randint(5000, 43000)
    time_to_buffet = random.randint(0, 100)
    time_from_buffet_to_uncommanded_descent = random.randint(0, 10)
    magnitude_of_uncommanded_descent = random.randint(time_from_buffet_to_uncommanded_descent + 1,
                                                      time_from_buffet_to_uncommanded_descent + 300)
    time_from_buffet_to_uncommanded_roll = random.randint(time_from_buffet_to_uncommanded_descent,
                                                          time_from_buffet_to_uncommanded_descent + 30)
    magnitude_of_uncommanded_roll = random.randint(0, 90)
    initial_airspeed = random.randint(120, 300)

    period_of_uncommanded_roll = np.random.normal(0, 10, 1)
    time_from_buffet_to_uncommanded_descent_high = random.randint(time_from_buffet_to_uncommanded_descent + 1,
                                                                  time_from_buffet_to_uncommanded_descent + 30)
    magnitude_of_uncommanded_descent_high = random.randint(120, 1200)
    time_from_buffet_to_positive_angle_of_attack = random.randint(time_from_buffet_to_uncommanded_descent + 1,
                                                                  time_from_buffet_to_uncommanded_descent + 10)
    max_angle_of_attack = random.randint(10, 30)
    rate_of_change_in_angle_of_attack = random.random()

    cur_time = 0
    alt_noise = round(np.random.normal(0, 5, 1)[0], 6)
    alt_noise_buffet = round(np.random.normal(0, 10, 1)[0], 6)
    airspeed_noise = round(np.random.normal(0, 5, 1)[0], 6)
    airspeed_noise_buffet = round(np.random.normal(0, 10, 1)[0], 6)
    cur_altitude = initial_alt
    cur_airspeed = initial_airspeed
    roll = 0
    vertical_speed = 0
    angle_of_attack = 0
    flight_path_angle = 0
    pitch_angle = 0

    return FlightData(
        flight_id,
        initial_alt,
        time_to_buffet,
        time_from_buffet_to_uncommanded_descent,
        magnitude_of_uncommanded_descent,
        time_from_buffet_to_uncommanded_roll,
        magnitude_of_uncommanded_roll,
        period_of_uncommanded_roll,
        initial_airspeed,
        time_from_buffet_to_uncommanded_descent_high,
        magnitude_of_uncommanded_descent_high,
        time_from_buffet_to_positive_angle_of_attack,
        max_angle_of_attack,
        rate_of_change_in_angle_of_attack,
        cur_time,
        alt_noise,
        alt_noise_buffet,
        airspeed_noise,
        airspeed_noise_buffet,
        cur_altitude,
        cur_airspeed,
        roll,
        vertical_speed,
        angle_of_attack,
        flight_path_angle,
        pitch_angle)


# generate flight record based on constants and past flight data
def generate_flight_record(flight_id, initial_alt, time_to_buffet, time_from_buffet_to_uncommanded_descent,
                           magnitude_of_uncommanded_descent, time_from_buffet_to_uncommanded_roll,
                           magnitude_of_uncommanded_roll, period_of_uncommanded_roll, initial_airspeed,
                           time_from_buffet_to_uncommanded_descent_high, magnitude_of_uncommanded_descent_high,
                           time_from_buffet_to_positive_angle_of_attack, max_angle_of_attack,
                           rate_of_change_in_angle_of_attack, past_time, past_alt, past_airspeed, past_angle_of_attack):
    initial_alt = initial_alt

    time_to_buffet = time_to_buffet
    time_from_buffet_to_uncommanded_descent = time_from_buffet_to_uncommanded_descent
    magnitude_of_uncommanded_descent = magnitude_of_uncommanded_descent
    time_from_buffet_to_uncommanded_roll = time_from_buffet_to_uncommanded_roll
    magnitude_of_uncommanded_roll = magnitude_of_uncommanded_roll
    initial_airspeed = initial_airspeed
    period_of_uncommanded_roll = period_of_uncommanded_roll
    time_from_buffet_to_uncommanded_descent_high = time_from_buffet_to_uncommanded_descent_high
    magnitude_of_uncommanded_descent_high = magnitude_of_uncommanded_descent_high
    time_from_buffet_to_positive_angle_of_attack = time_from_buffet_to_positive_angle_of_attack
    max_angle_of_attack = max_angle_of_attack
    rate_of_change_in_angle_of_attack = rate_of_change_in_angle_of_attack

    cur_time = past_time + .1
    delta_time = cur_time - past_time
    alt_noise = round(np.random.normal(0, 5, 1)[0], 6)
    alt_noise_buffet = round(np.random.normal(0, 10, 1)[0], 6)
    airspeed_noise = round(np.random.normal(0, 5, 1)[0], 6)
    airspeed_noise_buffet = round(np.random.normal(0, 10, 1)[0], 6)
    cur_alt = initial_alt + alt_noise
    if cur_time > time_from_buffet_to_uncommanded_descent_high:
        cur_alt = round(past_alt - (magnitude_of_uncommanded_descent_high / delta_time) + alt_noise, 6)
    elif cur_time > time_from_buffet_to_uncommanded_descent:
        cur_alt = round(past_alt - (magnitude_of_uncommanded_descent / delta_time) + alt_noise, 6)
    elif cur_time > (time_from_buffet_to_uncommanded_descent - 5):
        cur_alt = initial_alt + alt_noise_buffet

    vertical_speed = round((cur_alt - past_alt) / delta_time, 6)

    angle_of_attack = 0
    if cur_time > time_from_buffet_to_positive_angle_of_attack:
        if past_angle_of_attack + rate_of_change_in_angle_of_attack > max_angle_of_attack:
            angle_of_attack = max_angle_of_attack
        else:
            angle_of_attack = past_angle_of_attack + rate_of_change_in_angle_of_attack

    cur_airspeed = initial_airspeed + airspeed_noise
    if cur_time > time_to_buffet:
        cur_airspeed = past_airspeed + airspeed_noise_buffet

    flight_path_angle = 0

    if airspeed_noise != 0:
        flight_path_angle = round(np.arcsin(vertical_speed / cur_airspeed), 6)

    pitch_angle = flight_path_angle + angle_of_attack

    roll = 0
    if cur_time > time_from_buffet_to_uncommanded_roll:
        roll = np.sin(flight_path_angle)

    return FlightData(
        flight_id,
        initial_alt,
        time_to_buffet,
        time_from_buffet_to_uncommanded_descent,
        magnitude_of_uncommanded_descent,
        time_from_buffet_to_uncommanded_roll,
        magnitude_of_uncommanded_roll,
        period_of_uncommanded_roll,
        initial_airspeed,
        time_from_buffet_to_uncommanded_descent_high,
        magnitude_of_uncommanded_descent_high,
        time_from_buffet_to_positive_angle_of_attack,
        max_angle_of_attack,
        rate_of_change_in_angle_of_attack,
        cur_time,
        alt_noise,
        alt_noise_buffet,
        airspeed_noise,
        airspeed_noise_buffet,
        cur_alt,
        cur_airspeed,
        roll,
        vertical_speed,
        angle_of_attack,
        flight_path_angle,
        pitch_angle)
