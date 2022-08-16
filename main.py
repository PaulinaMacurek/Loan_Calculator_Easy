import math
import argparse
import sys

parser = argparse.ArgumentParser(description="This program calculate some loan parametrs.")

parser.add_argument("--type", choices=["annuity", "diff"],
                    help="You need to choose only one option from the list.")
parser.add_argument("--payment", type=int,
                    help="'--payment' is the monthly payment amount. Valid only with '--type = annuity'.")
parser.add_argument("--principal", type=int,
                    help="Enter the loan principal.")
parser.add_argument("--interest", type=float,
                    help="Enter interest without a percent sign.")
parser.add_argument("--periods", type=int,
                    help="Enter how many months do you want to repay your loan?.")
args = parser.parse_args()  # The parse_args() method is used for reading argument strings from the command line


type_of_calc = args.type
loan_principal = args.principal
monthly_payment = args.payment
nr_periods = args.periods
loan_interest = args.interest

def check_type(type):
    if type is not None:
        return type if type in ["diff", "annuity"] else False


def months_to_years(nr_months_to_calculate):
    nr_years, nr_months = divmod(nr_months_to_calculate, 12)
    if nr_years >= 1 and nr_months >= 1:
        print(f"It will take {nr_years}", "years" if nr_years != 1 else "year",
        f"and {nr_months} months" if nr_months != 1 else "month", "to repay this loan!")
    elif nr_years == 0 and nr_months >= 1:
        print(f"It will take {nr_months}", "months" if nr_months != 1 else "month", "to repay this loan!")
    else:
        print(f"It will take {nr_years}", "years" if nr_years != 1 else "year", "to repay this loan!")
    overpayment = nr_months_to_calculate * monthly_payment - loan_principal
    if overpayment:
        print(f"Overpayment = {overpayment}")


def nbr_monthly_payments():
    result = math.ceil(math.log(monthly_payment / (monthly_payment - loan_interest * loan_principal), 1 + loan_interest))
    return result


def annuity_monthly_payment_amount():
    result = math.ceil(loan_principal * (loan_interest * (1 + loan_interest) ** nr_periods) / ((1 + loan_interest) ** nr_periods - 1))
    print(f"Your monthly payment = {result}!")
    overpayment = result * nr_periods - loan_principal
    if overpayment:
        print(f"Overpayment = {overpayment}")


def loan_principal_fun():
    result = round(
        monthly_payment * ((1 + loan_interest) ** nr_periods - 1) / (loan_interest * (1 + loan_interest) ** nr_periods))
    print(f"Your loan principal = {result}!")
    return result


def differentiated_payments():
    suma = 0
    for i in range(1, nr_periods + 1):
        result = loan_principal / nr_periods + loan_interest * (loan_principal - (i - 1) * loan_principal / nr_periods)
        result = math.ceil(result)
        print(f"Month {i}: payment is {result}")
        suma += result
    overpayment = suma - loan_principal
    if overpayment:
        print(f"\nOverpayment = {overpayment}")


parametrs = [monthly_payment, loan_principal, loan_interest, nr_periods]
for item in parametrs:
    if item == None:
        continue
    elif item < 0:
        print("Incorrect parameters")
        sys.exit(0)

if loan_interest != None:
    loan_interest=loan_interest/1200

if check_type(type_of_calc) == 'diff':
    if not monthly_payment and loan_principal and nr_periods and loan_interest:
        differentiated_payments()
    else:
        print("Incorrect parameters")
        sys.exit(0)
elif check_type(type_of_calc) == "annuity":
    if monthly_payment and not loan_principal and nr_periods and loan_interest:
        loan_principal_fun()
    elif monthly_payment and loan_principal and not nr_periods and loan_interest:
        months_to_years(nbr_monthly_payments())
    elif not monthly_payment and loan_principal and nr_periods and loan_interest:
        annuity_monthly_payment_amount()
    else:
        print("Incorrect parameters")
        sys.exit(0)
else:
    print("Incorrect parameters")
