# Importing packages/functions
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error


def prep_training_test_sets(filename, final_parameter_column, test_size, pred_variable):
    dt = pd.read_csv(filename)
   #dt = pd.read_excel(open(filename, 'rb'), sheet_name=sheet_number)

    # Extracting static values (parameters)
    params = dt.iloc[:, 0:final_parameter_column]
    # Extracting flight data into its own dataframe
    df = dt.iloc[:, final_parameter_column + 1:(len(dt) - 1)]
    y = df[pred_variable]
    x = df.drop(pred_variable, axis=1)

    # Generating training and test sets
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)

    # Saving datasets in a folder
    cwd = os.getcwd()
    set_names = ['x_train', 'x_test', 'y_train', 'y_test']
    sets = [x_train, x_test, y_train,  y_test]
    for n in range((len(sets))):
        sets[n].to_csv(f"{cwd}/RandomForestOutputs/{str(set_names[n])}.csv'")
        #sets[n].to_excel(cwd + '/RandomForestOutputs/' + str(set_names[n]) + '.xlsx')

    # Returning dimensions of full dataset, training, and test sets
    print(f"Variable to Predict: {pred_variable}")
    print(f"Dataset dimensions: {df.shape}")
    print(f"Training set dimensions: y:{y_train.shape} x:{x_train.shape}")
    print(f"Test set dimensions: y:{y_test.shape} x:{x_test.shape}")
    return x_train, x_test, y_train, y_test


def run_random_forest(x_train, x_test, y_train, y_test, num_trees):
    # Initialize Random Forest Regressor object
    rfm = RandomForestRegressor(n_estimators=num_trees)
    # Fit training data into regressor object
    rfm_fit = rfm.fit(x_train, y_train)
    # Run model on test data
    pred = rfm.predict(x_test)
    # Return Metrics
    print(f"MSE: {mean_squared_error(y_test, pred)}")
    print(f"RMSE: {np.sqrt(mean_squared_error(y_test, pred))}")
    print(f"R2 Score: {r2_score(y_test, pred)}")


if __name__ == '__main__':
    # Parameters for functions
    filename = 'stall_data.csv'
    #sheet_number
    final_parameter_column = 14  # Splits all the static parameters dataset. In this case, 14 is the last column with static data
    test_size = 0.3  # Size of test dataset
    pred_variable = 'vertical_speed'  # What we want the random forest to predict
    num_trees = 100

    # Prepare dataset for the model
    [x_train, x_test, y_train, y_test] = prep_training_test_sets(filename, final_parameter_column,
                                                                 test_size, pred_variable)
    # Run the random forest model
    run_random_forest(x_train, x_test, y_train, y_test, num_trees)
