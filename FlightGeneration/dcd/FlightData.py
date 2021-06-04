class FlightData:

    def __init__(self,
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
                 pitch_angle):
        self.pitch_angle = pitch_angle
        self.flight_path_angle = flight_path_angle
        self.angle_of_attack = angle_of_attack
        self.vertical_speed = vertical_speed
        self.roll = roll
        self.cur_airspeed = cur_airspeed
        self.cur_altitude = cur_altitude
        self.airspeed_noise_buffet = airspeed_noise_buffet
        self.cur_time = cur_time
        self.rate_of_change_in_angle_of_attack = rate_of_change_in_angle_of_attack
        self.max_angle_of_attack = max_angle_of_attack
        self.time_from_buffet_to_positive_angle_of_attack = time_from_buffet_to_positive_angle_of_attack
        self.magnitude_of_uncommanded_descent_high = magnitude_of_uncommanded_descent_high
        self.time_from_buffet_to_uncommanded_descent_high = time_from_buffet_to_uncommanded_descent_high
        self.period_of_uncommanded_roll = period_of_uncommanded_roll
        self.airspeed_noise = airspeed_noise
        self.initial_airspeed = initial_airspeed
        self.magnitude_of_uncommanded_roll = magnitude_of_uncommanded_roll
        self.time_from_buffet_to_uncommanded_roll = time_from_buffet_to_uncommanded_roll
        self.magnitude_of_uncommanded_descent = magnitude_of_uncommanded_descent
        self.time_from_buffet_to_uncommanded_descent = time_from_buffet_to_uncommanded_descent
        self.time_to_buffet = time_to_buffet
        self.alt_noise_buffet = alt_noise_buffet
        self.alt_noise = alt_noise
        self.initial_alt = initial_alt
        self.flight_id = flight_id


    def to_dict(self):
        return {
            'flight_id': self.flight_id,
            'initial_alt': self.initial_alt,
            'time_to_buffet': self.time_to_buffet,
            'time_from_buffet_to_uncommanded_descent': self.time_from_buffet_to_uncommanded_descent,
            'magnitude_of_uncommanded_descent': self.magnitude_of_uncommanded_descent,
            'time_from_buffet_to_uncommanded_roll': self.time_from_buffet_to_uncommanded_roll,
            'magnitude_of_uncommanded_roll': self.magnitude_of_uncommanded_roll,
            'period_of_uncommanded_roll': self.period_of_uncommanded_roll,
            'initial_airspeed': self.initial_airspeed,
            'time_from_buffet_to_uncommanded_descent_high': self.time_from_buffet_to_uncommanded_descent_high,
            'magnitude_of_uncommanded_descent_high': self.magnitude_of_uncommanded_descent_high,
            'time_from_buffet_to_positive_angle_of_attack': self.time_from_buffet_to_positive_angle_of_attack,
            'max_angle_of_attack': self.max_angle_of_attack,
            'rate_of_change_in_angle_of_attack': self.rate_of_change_in_angle_of_attack,
            'cur_time': self.cur_time,
            'alt_noise': self.alt_noise,
            'alt_noise_buffet': self.alt_noise_buffet,
            'airspeed_noise': self.airspeed_noise,
            'airspeed_noise_buffet': self.airspeed_noise_buffet,
            'cur_altitude': self.cur_altitude,
            'cur_airspeed': self.cur_airspeed,
            'roll': self.roll,
            'vertical_speed': self.vertical_speed,
            'angle_of_attack': self.angle_of_attack,
            'flight_path_angle': self.flight_path_angle,
            'pitch_angle': self.pitch_angle
        }
