# Packages for creating the graphs

from pickle import TRUE
from linear_regression_model import LinearRegressionModel

import csv
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":

    input_path = './source/input_data.csv'

    print('\n*****  Welcome!   ***** \n\n This app implements a simple linear regression model.')
    print('This Bonus Task has been completed using Python3 and the matplotlib library') 
    print('\nI hope you enjoy - Lachlan Pearce')

    input("\nPlease Press Enter to continue...")

    #Importing Values from csv file to individual arrays
    with open(input_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        xValue = [] 
        yValue = []
        for row in csv_reader:
            xValue.append(row[0])
            yValue.append(row[1])
        
    #Converting Array of Str to Array of float
    xValueInt = [float(numeric_string) for numeric_string in xValue]
    yValueInt = [float(numeric_string) for numeric_string in yValue]

    input_values = []
    
    #Taking user input for value prediction. Must be a number (float or int is fine). Error thrown if not number
    print('Please enter your first test value then press enter, or leave blank and press enter to continue with no test values')
    while True:
        userInput = input() 
        if not userInput:
            if len(input_values) != 0:
                 print('Awesome thank you!','\n')
            else:
                print('Really!? No test values?...\n')
            break
        try:
            float(userInput)
            if userInput:
              input_values.append(userInput)
              print('Please enter another value or leave blank and press enter to continue')
        except ValueError:
            print("Sorry this is not a number try again")
            
       
    inputValues = [float(numeric_string) for numeric_string in input_values]

    print('The X Values from the input_data.csv file are:', xValueInt)
    print('The Y Values from the input_data.csv file are:', yValueInt)


    if len(input_values) != 0:
        print('\nTherefore, based on your test values, and the data provided in the input_data.csv file')
        response_values, beta, alpha = LinearRegressionModel.cal_simple_linear_regression_coefficients(xValueInt, yValueInt, inputValues)
    else:
        print('\nTherefore, based on the data provided in the input_data.csv file')
        beta, alpha = LinearRegressionModel.cal_simple_linear_regression_coefficients(xValueInt, yValueInt, inputValues)


    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    x = np.linspace(-20,20,100)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.xlim(-15, 15)
    plt.ylim(-15,15)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.scatter(xValueInt, yValueInt, label='Input Data')
    if len(inputValues) != 0:
        ax.plot(inputValues,response_values,'go', label='Predicted Response Value')
    ax.plot(x, x*alpha+beta, '-r', label='Regression Line')
    plt.legend(loc='upper left')
    plt.show()


  