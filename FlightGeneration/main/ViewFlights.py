import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    df = pd.read_excel(open('stall_data.xlsx', 'rb'), sheet_name='sheet_data_0')

    fig, axs = plt.subplots(10)
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
    axs[7].plot(df['cur_time'], df['cur_avg_altitude'])
    axs[7].set_title('cur_time vs cur_avg_altitude')
    axs[8].plot(df['cur_time'], df['cur_avg_airspeed'])
    axs[8].set_title('cur_time vs cur_avg_airspeed')
    axs[9].plot(df['cur_time'], df['cur_avg_vertical_speed'])
    axs[9].set_title('cur_time vs cur_avg_vertical_speed')
    plt.show()
