'''Build a mortgage calculator to determine monthly payments, with monthly interest

You will need three pieces of information:
1. the loan amount
2. the Annual Percentage Rate (APR)
3. the loan duration

from the above you will need to calculate the following things:

1. Monthly interest rate (APR/12)
2. loan duration in months

You can use the following formula:

m = p*(j/(1-(1+j)**(-n)))

m = month payment
p = loan amount
j = monthly interest rate
n = loan duration in months

-dont use single letters to write the program
-print payment amount as dollars with 2 decimals
-dont forget to run your code with Pylint '''


# 0.0 define prompt function
def prompt(message):
    '''Display a formatted prompt message'''
    print(f"=> {message}")


def calculate_monthly_interest_rate(apr_percent):
    '''Calculate monthly interest rate from APR'''
    return float(apr_percent)/12/100 # divided between 100 to transform percent into number that can be used in formula (5% -> 0.05)


def calculate_loan_duration_months(annual_loan_duration):
    '''Convert years to months'''
    return int(float(annual_loan_duration) * 12)


#     m = p*(j/(1-(1+j)**(-n)))
def calculate_monthly_payment(loan_amount, monthly_rate, loan_duration_months):
    '''Calculate the monthly payment'''
    loan_amount = float (loan_amount)
    if monthly_rate == 0:
        return loan_amount / loan_duration_months
    return loan_amount * (monthly_rate/ (1 - ( 1 + monthly_rate) ** (-loan_duration_months)))


def is_invalid_number(number_str):
    '''Returns True if value cannot be converted to a positive float'''
    try:
        value = float(number_str) # float to allow for decimals
        if value <= 0:
            raise ValueError(f'Value must be > 0: {number_str}')
    except ValueError:
        return True

    return False

# # 1. Introduce the program
prompt('Welcome to Mortgage Calculator!')

while True:

    # 2. get loan amount ($0.00) - make sure input is valid
    prompt('Insert loan amount $')
    loan_amount = input()

    while is_invalid_number(loan_amount):
        prompt('invalid value, insert a positive number')
        loan_amount = input()

    # 3. get APR (0.0-99.9%) - make sure input is valid
    prompt('Insert the annual percent rate (APR) with a value from 0.0 to 100.0')
    apr_percent = input()

    while True:
        apr_value = float (apr_percent)
        if 0.0 <= apr_value <= 100.0:
            break
        prompt('invalid value, insert an APR value from 0.0 to 100.0')
        apr_percent = input()

    # 4. get loan duration
    prompt('Insert loan duration in years')
    annual_loan_duration = input()

    while is_invalid_number(annual_loan_duration):
        prompt('invalid value, insert a positive number')
        annual_loan_duration = input ()

    # 4. Calculate values
    monthly_rate = calculate_monthly_interest_rate(apr_percent)
    loan_duration_months = calculate_loan_duration_months(annual_loan_duration)
    monthly_payment = calculate_monthly_payment(loan_amount, monthly_rate, loan_duration_months)

    # 5. Display results
    prompt(f'The monthly interest rate is {monthly_rate:.4f}')
    prompt(f'the loan duration is {loan_duration_months} months')
    prompt(f'the monthly payment is ${monthly_payment:.2f}')
    # round numbers after calculations in the printing step with f-strings

    # 6. Ask if user wants to calculate another loan
    prompt('Would you like to calculate another Mortgage?: y/n')
    answer = input().lower()

    if not answer or answer[0] != 'y':
        break
    #We use "and" operator to check an empty case and make sure that if it is an empty string doesn't raise an IndexError
