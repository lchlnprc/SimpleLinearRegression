# Simple Linear Regression Using No External Packages
  * Lachlan Pearce

My solution application runs solely on Python, executing the Primary linear regression using only the Python standard 
libraries. My Bonus Section uses the external library matplotlib included in the requirements.txt file to 
visualise a scatter plot of the data stored in the input_data.csv. A regression line through these points is 
also displayed, and if test values are entered, their predicted values are also shown.


# Requirements

  * Python 3.10.0

All development and testing was executed using Python 3.10.0, while other versions of Python3 may work,
they have not been tested, particularly with the specified external library for the bonus section. 

# Execution and Output of the Primary Task

To run the primary task using command line arguments, a virtual environment is not necessary provided Python3
is installed locally and the command line directory is set to this directory. Since this task only uses standard
libraries it can be executed directly using:

```
py linear_regression_model.py
```

After following the prompts, and entering the chosen test data values, the following output message will be displayed.

```
Therefore, based on your test values, and the data provided in the input_data.csv file
alpha = 1.4
beta  = 3.5
input_values    = [2.5, 3.5]
response_values = [7.0, 8.4]
RMSE            = 1.05
```
Note that specific output values will vary dependant on the input values.

# Execution and Output of Bonus Task (Visualisation) on Windows

To run the bonus task using command line arguments, a virtual environment is recommended to safely store the 
required external library matplotlib. Matplotlib is a plotting library for the Python programming language and its 
numerical mathematics extension NumPy. To execute this, a virtual environment must first be set up:
```
py -m pip install --user virtualenv
py -m venv env
.\env\Scripts\activate
```
After executing the above commands, the command line should now begin with:
```
(env) C:\...
```
Once inside the virtual environment, the required packages must be installed using:
```
pip install -r requirements.txt
```
Once this has successfully installed, the visualisation model can be executed using:
```
py linear_regression_visualisation.py
```
After following the prompts, and entering the chosen test data values, the following output message will be displayed
along with a visual plot of the data. The command line return will look similar to the following:
```
Therefore, based on your test values, and the data provided in the input_data.csv file
alpha = 1.4
beta  = 3.5
input_values    = [2.5, 3.5]
response_values = [7.0, 8.4]
RMSE            = 1.05
```
Note that specific output values will vary dependant on the input values. An interactive visualisation of the data will 
also be displayed in a new pop up window showing the original data, the linear regression line, and any predicted data
if test input values were given.

# Execution and Output of Bonus Task (Visualisation) on Unix/macOS

The setup of this is very similar to Windows bar the creation of the virtual environment. This must be set using:
```
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
```
Once the virtual environment is set up, execution is the same as Windows shown above. 

# Input Data Stored in input_data.csv

The input data used as a source for the simple linear regression model is stored under the file './source/input_data.csv'.
To edit this data, X values are stored in column 0 & Y values are stored in column 1. 

# Unit Testing 

Unit tests can be executed within or outside of a virtual environment as the testing comes from the Python standard library.
To execute the unit testing:

```
py unit_test.py
```

A successful test pass will output similar to the following:

```
alpha =  1.4
beta =  3.5
.alpha =  1.4
beta =  3.5
response_values = [7.0, 8.4]
.
----------------------------------------------------------------------
Ran 2 tests in 0.012s

OK
```
Current Unit Tests:

    -Testing that no predicted data is attempted to be made when no test data is given in command line input. As such there
    should only be two returns from the application not three.

    -Testing that all return values are correct based on the example data given in the Technical Evaluation Worksheet PDF.

