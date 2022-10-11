#Implementing a simple linear regression model using only Python Standard Libraries
#Author: Lachlan Pearce
#14 September 2022

import csv

from math import pow

class LinearRegressionModel:

    def cal_mean(readings):
        """
        Function to calculate the mean value of the input readings
        :param readings:
        :return:
        """
        readings_total = sum(readings)
        number_of_readings = len(readings)
        mean = readings_total / float(number_of_readings)
        return mean
    
    
    def cal_variance(readings):
        """
        Calculating the variance of the readings
        :param readings:
        :return:
        """
    
        # To calculate the variance we need the mean value
        # Calculating the mean value from the cal_mean function
        readings_mean = LinearRegressionModel.cal_mean(readings)
        # mean difference squared readings
        mean_difference_squared_readings = [pow((reading - readings_mean), 2) for reading in readings]
        variance = sum(mean_difference_squared_readings)
        return variance / float(len(readings) - 1)
    
    
    def cal_covariance(readings_1, readings_2):
        """
        Calculate the covariance between two different list of readings
        :param readings_1:
        :param readings_2:
        :return:
        """
        readings_1_mean = LinearRegressionModel.cal_mean(readings_1)
        readings_2_mean = LinearRegressionModel.cal_mean(readings_2)
        readings_size = len(readings_1)
        covariance = 0.0
        for i in range(0, readings_size):
            covariance += (readings_1[i] - readings_1_mean) * (readings_2[i] - readings_2_mean)
        return covariance / float(readings_size - 1)
    
    
    def cal_simple_linear_regression_coefficients(x_readings, y_readings,input_values):
        """
        Calculating the simple linear regression coefficients (beta, alpha)
        :param x_readings:
        :param y_readings:
        :return:
        """
        # Coefficient alpha = covariance of x_readings and y_readings divided by variance of x_readings
        # Directly calling the implemented covariance and the variance functions
        # To calculate the coefficient alpha
        alpha = LinearRegressionModel.cal_covariance(x_readings, y_readings) / float(LinearRegressionModel.cal_variance(x_readings))
    
        # Coefficient beta = mean of y_readings - ( alpha * the mean of the x_readings )
        beta = LinearRegressionModel.cal_mean(y_readings) - (alpha * LinearRegressionModel.cal_mean(x_readings))

        print('alpha =', round(alpha,4))
        print('beta  =', round(beta,4))

        ##Calculating the RMSE
        yRegression = []

        for i in range(0, len(y_readings)):
            yRegression.append(round((alpha*(x_readings[i])+beta),4))

        rmse = LinearRegressionModel.cal_rmse(y_readings,yRegression)

        if len(input_values) != 0:
            response_values = LinearRegressionModel.predict_target_value(input_values, beta, alpha)
            print('input_values    =', input_values)
            print('response_values =', response_values)
            print('RMSE            =', round(rmse,4))
            beta = round(beta,4)
            alpha = round(alpha, 4)
            return response_values, beta, alpha

        else:
            beta = round(beta,4)
            alpha = round(alpha, 4)
            print('RMSE  =', round(rmse,4))
            return beta, alpha
    
    
    def predict_target_value(input_values, beta, alpha):
        """
        Calculating the target (y) value using the input x and the coefficients beta, alpha
        :param x:
        :param beta:
        :param alpha:
        :return:
        """

        response_values = []
        
        for x in range(len(input_values)):
            response_values.append(round((beta+(alpha*input_values[x])),4))

        return response_values
    
    
    def cal_rmse(actual_readings, predicted_readings):
        """
        Calculating the root mean square error
        :param actual_readings:
        :param predicted_readings:
        :return:
        """
        square_error_total = 0.0
        total_readings = len(actual_readings)
        for i in range(0, total_readings):
            error = predicted_readings[i] - actual_readings[i]
            square_error_total += pow(error, 2)
        rmse = square_error_total / float(total_readings)
        return rmse
    
    
    
if __name__ == "__main__":
 
    input_path = './source/input_data.csv'

    print('\n*****  Welcome!   ***** \n\n This app implements a simple linear regression model.')
    print('This Primary Task has been completed using only Python3 Standard Libraries.') 
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
    else:
        print('\nTherefore, based on the data provided in the input_data.csv file')
    LinearRegressionModel.cal_simple_linear_regression_coefficients(xValueInt, yValueInt, inputValues)

    
   