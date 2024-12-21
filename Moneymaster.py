import csv
import datetime

# Function to get a positive float input from the user
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                print("Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Function to get a valid integer input
def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            if value <= 0:
                print("Value must be greater than zero. Please try again.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main calculator function
def rule_of_72():
    print("Welcome to the Financial Calculator!")

    while True:
        print("\nSelect an option:")
        print("1. Rule of 72: Years to Double or Rate of Return")
        print("2. Compound Interest")
        print("3. Future Value of Investment")
        print("4. Present Value of Investment")
        print("5. Loan Payment (PMT)")
        print("Type 'exit' to quit.")

        choice = input("Enter your choice (1-5 or 'exit' to quit): ").strip().lower()

        if choice == 'exit':
            print("Thank you for using the Financial Calculator. Goodbye!")
            break
        
        if choice == "1":
            rule_of_72_calculation()
        
        elif choice == "2":
            compound_interest_calculation()
        
        elif choice == "3":
            future_value_calculation()
        
        elif choice == "4":
            present_value_calculation()
        
        elif choice == "5":
            loan_payment_calculation()

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")
        
        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using the Financial Calculator. Goodbye!")
            break

# Rule of 72
def rule_of_72_calculation():
    print("\n--- Rule of 72 ---")
    choice = input("Would you like to calculate (1) Years to Double or (2) Rate of Return? Enter 1 or 2: ").strip()

    if choice == "1":
        rate_of_return = get_positive_float("Enter the annual rate of return (in percentage, e.g., 6 for 6%): ")
        years_to_double = 72 / rate_of_return
        print(f"With an annual return of {rate_of_return}%, it will take approximately {years_to_double:.2f} years to double your investment.")
        save_to_file(f"Rule of 72: {rate_of_return}% return = {years_to_double:.2f} years to double")
    
    elif choice == "2":
        years_to_double = get_positive_float("Enter the number of years it will take to double your investment: ")
        rate_of_return = 72 / years_to_double
        print(f"To double your investment in {years_to_double} years, you need an annual rate of return of approximately {rate_of_return:.2f}%.")
        save_to_file(f"Rule of 72: {years_to_double} years = {rate_of_return:.2f}% return")
    else:
        print("Invalid choice.")

# Compound Interest Formula: A = P(1 + r/n)^(nt)
def compound_interest_calculation():
    print("\n--- Compound Interest ---")
    principal = get_positive_float("Enter the principal amount ($): ")
    rate = get_positive_float("Enter the annual interest rate (in %): ") / 100
    time = get_positive_float("Enter the time (in years): ")
    comp_per_year = get_positive_int("Enter the number of times interest is compounded per year: ")

    if comp_per_year == 0:
        print("Compounding periods per year must be greater than zero.")
        return

    amount = principal * (1 + rate / comp_per_year) ** (comp_per_year * time)
    interest = amount - principal

    print(f"After {time} years, your investment will grow to ${amount:.2f}. The interest earned is ${interest:.2f}.")
    save_to_file(f"Compound Interest: P=${principal}, r={rate*100}%, Time={time} years, A=${amount:.2f}, Interest=${interest:.2f}")

# Future Value of Investment: FV = PV * (1 + r)^t
def future_value_calculation():
    print("\n--- Future Value of Investment ---")
    present_value = get_positive_float("Enter the present value ($): ")
    rate_of_return = get_positive_float("Enter the annual rate of return (in %): ") / 100
    time = get_positive_float("Enter the time (in years): ")

    future_value = present_value * (1 + rate_of_return) ** time
    print(f"The future value of your investment will be ${future_value:.2f}.")
    save_to_file(f"Future Value: PV=${present_value}, r={rate_of_return*100}%, Time={time} years, FV=${future_value:.2f}")

# Present Value of Investment: PV = FV / (1 + r)^t
def present_value_calculation():
    print("\n--- Present Value of Investment ---")
    future_value = get_positive_float("Enter the future value ($): ")
    rate_of_return = get_positive_float("Enter the annual rate of return (in %): ") / 100
    time = get_positive_float("Enter the time (in years): ")

    present_value = future_value / (1 + rate_of_return) ** time
    print(f"The present value of the investment is ${present_value:.2f}.")
    save_to_file(f"Present Value: FV=${future_value}, r={rate_of_return*100}%, Time={time} years, PV=${present_value:.2f}")

# Loan Payment (PMT) Formula: PMT = P * [r(1 + r)^n] / [(1 + r)^n - 1]
def loan_payment_calculation():
    print("\n--- Loan Payment (PMT) ---")
    principal = get_positive_float("Enter the loan amount ($): ")
    annual_rate = get_positive_float("Enter the annual interest rate (in %): ") / 100
    years = get_positive_int("Enter the loan term (in years): ")

    monthly_rate = annual_rate / 12
    months = years * 12

    payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    print(f"The monthly payment is ${payment:.2f}.")
    save_to_file(f"Loan Payment: Loan=${principal}, r={annual_rate*100}%, Years={years}, Monthly Payment=${payment:.2f}")

# Function to save results to a CSV file
def save_to_file(result):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("financial_calculations.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, result])
    print(f"Result saved to file at {timestamp}.")

# Call the main function to run the program
rule_of_72()
