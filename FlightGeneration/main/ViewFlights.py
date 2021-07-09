import matplotlib.pyplot as plt
import pandas as pd
import os


def lineplots_flight_sim(cols, time, df, n):
    # Generates lineplots for each dataframe over a set of columns against time. N is used to determine its place in
    # the resulting subplot
    cwd = os.getcwd()
    fig, axs = plt.subplots(nrows, 1, figsize=(16, 8))
    for col, ax in zip(cols, axs.flatten()):
        ax.grid()
        ax.plot(time, df[col])
        ax.set_title(col + ' vs ' + time.name + ' (scale: 10 = 1s)')
    plt.subplots_adjust(hspace=1, wspace=0.1)
    fig.suptitle(f"Flight Data Simulations - Simulation:{df['flight_id'].unique()}", y=0.92)
    fig.savefig(cwd + '/visuals/' + 'flight_data' + str(n) + '.png')
    plt.show()
    plt.close()


if __name__ == '__main__':
    df = pd.read_csv('stall_data.csv')
    cols = ['cur_altitude', 'cur_airspeed', 'vertical_speed', 'roll', 'angle_of_attack', 'flight_path_angle',
            'pitch_angle', 'cur_avg_altitude', 'cur_avg_airspeed', 'cur_avg_vertical_speed', 'cur_avg_flight_path_angle']
    nrows = 6
    flight_ids = df['flight_id'].unique()
    # Loops through each flight id and generates a visualization for each flight simulation (title indicates number)
    for i in flight_ids:
        df_flight_sim = df.loc[df['flight_id'] == i]
        time = df_flight_sim['cur_time']
        split_cols = [cols[i * nrows:(i + 1) * nrows] for i in range((len(cols) + nrows - 1) // nrows)]
        for n in range(len(split_cols)):
            lineplots_flight_sim(split_cols[n], time, df_flight_sim, n)