import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# Create lineplots for various data fields (columns) over a single time column (time) and places the resulting output
# into a "visuals" directory
def lineplots_flight_data(cols, time, df):
    cwd = os.getcwd()
    fig, axs = plt.subplots(len(cols), figsize=(len(cols)*3, len(cols)*4))
    for i in range(len(cols)):
        axs[i].grid()
        axs[i].plot(time, cols[i], data=df)
        axs[i].set_ylabel(cols[i], rotation='horizontal', horizontalalignment='center', fontsize=10, labelpad=50)
        axs[i].set_xlabel(time.name)
        axs[i].set_xticks(np.arange(0, max(time), 1.0))
        #axs[i].set_yticks(np.arange(min(df[cols[i]], max(df[cols[i]]), abs((max(df[cols[i]]) - min(df[cols[i]])/5)))))
    plt.subplots_adjust(hspace=1, wspace=0.001)
    fig.suptitle('Flight Data Simulations', y=0.92)
    fig.savefig(cwd + '/visuals/' + 'flight_data.png')
    plt.show()

if __name__ == '__main__':
    df = pd.read_excel(open('stall_data.xlsx', 'rb'), sheet_name='sheet_data_1')
    cols = ['cur_altitude', 'cur_airspeed', 'vertical_speed','angle_of_attack', 'flight_path_angle', 'pitch_angle', 'roll', 'rate_of_change_in_angle_of_attack']
    time = df['cur_time']
    lineplots_flight_data(cols, time, df) # Runs the function for ONLY the first sheet in the excel document
