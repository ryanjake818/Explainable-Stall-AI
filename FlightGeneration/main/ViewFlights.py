import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


def lineplots_flight_data(cols, time, df, n):
    cwd = os.getcwd()
    fig, axs = plt.subplots(nrows, 1, figsize=(20, 15))
    for col, ax in zip(cols, axs.flatten()):
        ax.grid()
        ax.plot(time, df[col])
        ax.set_title(col + ' vs ' + time.name + '(s)')
        ax.set_xticks(np.arange(min(time), max(time) + 10, 10.0))
    plt.subplots_adjust(hspace=1, wspace=0.1)
    fig.suptitle('Flight Data Simulations', y=0.92)
    fig.savefig(cwd + '/visuals/' + 'flight_data' + str(n) + '.png')
    plt.show()
    plt.close()


if __name__ == '__main__':
    df = pd.read_excel(open('stall_data.xlsx', 'rb'), sheet_name='sheet_data_0')
    cols = ['cur_altitude', 'cur_airspeed', 'vertical_speed', 'angle_of_attack', 'flight_path_angle', 'pitch_angle',
            'roll', 'cur_avg_altitude', 'cur_avg_airspeed', 'cur_avg_vertical_speed', 'cur_avg_flight_path_angle']
    time = df['cur_time']
    nrows = 4  # How many figures you want in a single plot
    # Using list comprehension (https://www.geeksforgeeks.org/break-list-chunks-size-n-python/) to break up cols list into chunks based on nrows
    split_cols = [cols[i * nrows:(i + 1) * nrows] for i in range((len(cols) + nrows - 1) // nrows)]
    for n in range(len(split_cols)):
        lineplots_flight_data(split_cols[n], time, df, n)
