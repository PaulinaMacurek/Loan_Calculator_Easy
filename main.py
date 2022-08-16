import math
import argparse

parse = argparse.Aargparse.ArgumentParser(description="This program calculate some loan parametrs.")


def months_to_years(nr_months_to_calculate):
    nr_years = math.floor(nr_months_to_calculate / 12)
    nr_months = nr_months_to_calculate - nr_years * 12
    return [nr_years, nr_months]


def nbr_monthly_payments():
    print(msgs["msg_1"])
    loan_principal = int(input())
    print(msgs["msg_3"])
    monthly_payment = int(input())
    print(msgs["msg_5"])
    loan_interest = float(input()) / 1200  # divide by 12 and 100
    result = math.ceil(
        math.log(monthly_payment / (monthly_payment - loan_interest * loan_principal), 1 + loan_interest))
    return result


def annuity_monthly_payment_amount():
    print(msgs["msg_1"])
    loan_principal = int(input())
    print(msgs["msg_6"])
    nr_periods = int(input())
    print(msgs["msg_5"])
    loan_interest = float(input()) / 1200  # divide by 12 and 100
    result = math.ceil(
        loan_principal * (loan_interest * (1 + loan_interest) ** nr_periods) / ((1 + loan_interest) ** nr_periods - 1))
    print(f"Your monthly payment = {result}!")
    overpayment = result * nr_periods - loan_principal
    if overpayment:
        print(f"Overpayment = {overpayment}")


def loan_principal():
    print(msgs["msg_7"])
    annuity_payment = float(input())
    print(msgs["msg_6"])
    nr_periods = int(input())
    print(msgs["msg_5"])
    loan_interest = float(input()) / 1200  # divide by 12 and 100
    result = round(
        annuity_payment * ((1 + loan_interest) ** nr_periods - 1) / (loan_interest * (1 + loan_interest) ** nr_periods))
    print(f"Your loan principal = {result}!")
    return result


def differentiated_payments():
    print(msgs["msg_1"])
    loan_principal = int(input())
    print(msgs["msg_6"])
    nr_periods = int(input())
    print(msgs["msg_5"])
    loan_interest = float(input()) / 1200  # divide by 12 and 100
    suma = 0
    for i in range(1, nr_periods + 1):
        result = loan_principal / nr_periods + loan_interest * (loan_principal - (i - 1) * loan_principal / nr_periods)
        result = math.ceil(result)
        print(f"Month {i}: payment is {result}")
        suma += result
    overpayment = suma - loan_principal
    if overpayment:
        print(f"\nOverpayment = {overpayment}")


# wieczorem zrobiłam diggerentiated_payments() oraz annuity_monthly_payment_amount():

msgs = {"msg_1": "Enter the loan principal:",
        "msg_2": "What do you want to calculate? \ntype 'n' for number of monthly payments,\ntype 'a' for annuity monthly payment amount,\ntype 'p' for loan principal",
        "msg_3": "Enter the monthly payment:",
        "msg_4": "Enter the number of months:",
        "msg_5": "Enter the loan interest:",
        "msg_6": "Enter the number of periods:",
        "msg_7": "Enter the annuity payment:"}

print(msgs["msg_2"])
choice = input()
if choice == "n":
    result = months_to_years(nbr_monthly_payments())
    if result[0] != 1:
        if result[1] == 0:
            print(f"It will take {result[0]} years to repay this loan!")
        elif result[1] == 1:
            print(f"It will take {result[0]} years and 1 month to repay this loan!")
        else:
            print(print(f"It will take {result[0]} years and {result[1]} months to repay this loan!"))
    elif result[0] == 1:
        if result[1] == 0:
            print(f"It will take 1 year to repay this loan!")
        elif result[1] == 1:
            print(f"It will take 1 year and 1 month to repay this loan!")
        else:
            print(print(f"It will take 1 year and {result[1]} months to repay this loan!"))
    elif result[0] == 0:
        if result[1] == 0:
            print(f"Somthing went wrong... you dont have to repay your loan")
        elif result[1] == 1:
            print(f"It will take 1 month to repay this loan!")
        else:
            print(print(f"It will take {result[1]} months to repay this loan!"))

elif choice == "a":
    annuity_monthly_payment_amount()
elif choice == "p":
    loan_principal()
else:
  pass#  differentiated_payments()

