# Calculator GUI
The Calculator GUI is a simple desktop calculator application built using the customtkinter library. It provides a graphical user interface for performing basic arithmetic calculations. This README will guide you through the features of the app, how to use it, and how it's structured.

# Features
Arithmetic Operations: Perform addition, subtraction, multiplication, and division operations.

Percentage Calculation: Calculate percentages of numbers.

Exponentiation: Calculate the result of raising a number to a power.

Clear Function: Clear the current input or result.

Delete Function: Delete the last entered character.

Error Handling: Displays "Error" in case of invalid expressions.

User-Friendly Interface: Intuitive buttons and input display for easy interaction.

# Requirements
Python 3.x
customtkinter library (Make sure it is installed before running the app)
You can install the customtkinter library using the following command:

`pip install customtkinter`

# Usage
Clone or download the repository containing the Calculator GUI code.

Open a terminal and navigate to the directory where the calculator_gui.py file is located.

Run the app by executing the following command:

`python calculator_gui.py`

The Calculator App window will open, allowing you to perform calculations.

# How to Use
The input field at the top displays the current expression.

Click the number buttons (0-9) to enter digits of the expression.

Click the arithmetic operation buttons (+, -, *, /) to perform operations.

Click the "=" button to calculate and display the result of the expression.

Click the "%" button to calculate the percentage of the current expression.

Click the "x^y" button to indicate exponentiation (x raised to the power of y).

Click the "C" button to clear the input field and start a new calculation.

Click the "Del" button to delete the last entered character.

The result of the calculation is displayed in the input field.

# Structure
The calculator_gui.py file contains the code for the Calculator GUI. It utilizes the customtkinter library for creating the graphical interface. The CalculatorApp class initializes the app's components and defines the button actions. The if __name__ == "__main__": block at the end runs the app when the script is executed.

# Contributions
Contributions to this repository are welcome! If you find any issues or want to add new features, feel free to fork the repository, make changes, and submit a pull request.

# License
This project is licensed under the MIT License, allowing you to use and modify the code freely.
