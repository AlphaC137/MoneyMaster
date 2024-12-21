# FinanceMate
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

**FinanceMate** is an intuitive and powerful financial calculator that helps you perform key financial calculations, including the Rule of 72, compound interest, future/present value of investments, and loan payments. It provides clear results, robust input validation, and logs all calculations for easy tracking.

## Features

- **Rule of 72**: Calculate the time it takes for an investment to double or the required rate of return.
- **Compound Interest**: Calculate the future value of investments with compound interest.
- **Future/Present Value**: Determine the future or present value of an investment based on rate of return and time.
- **Loan Payment (PMT)**: Calculate monthly loan payments using principal, interest rate, and loan term.
- **Input Validation**: Robust checks for valid, positive inputs to ensure accurate results.
- **CSV Logging**: Save calculation results to a CSV file with timestamps for easy tracking.

## Installation

To use **FinanceMate** locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/alphac137/FinanceMate.git

Navigate to the project directory:
```
cd FinanceMate
```
Ensure Python is installed (Python 3.6 or above):


Run the script:

```
python finance_calculator.py
```
This will launch the interactive calculator in your terminal.

# Usage

Once the program is running, you'll be prompted to choose from the following options:

Rule of 72: Calculate the time it takes for an investment to double or the required rate of return.
Compound Interest: Calculate the future value of an investment with compound interest.
Future Value: Calculate the future value of an investment based on its present value, rate of return, and time.
Present Value: Calculate the present value of an investment based on its future value, rate of return, and time.
Loan Payment: Calculate monthly payments for loans based on principal, interest rate, and loan term.
After performing a calculation, you'll be given the option to repeat or exit. Results are logged into a CSV file for future reference.

# Example

Here's an example of what the output might look like:
```
--- Rule of 72 ---
Enter the annual rate of return (in percentage, e.g., 6 for 6%): 6
With an annual return of 6%, it will take approximately 12.00 years to double your investment.
Result saved to file at 2024-12-21 14:30:45.
```
# Contributing

Contributions are welcome! If you'd like to contribute to FinanceMate, please fork the repository and create a pull request with your changes.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Author
AlphaC137

# Acknowledgments

Python for being the best tool for rapid development.
Libraries like csv and datetime for handling file I/O and timestamps.
markdown
