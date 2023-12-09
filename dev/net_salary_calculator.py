## L13 Prove: Assignment ##
#Developer: Bruno Souza
#Course: CSE 111 - Programing with functions


import csv
from datetime import datetime
import time
import pandas as pd



def main():
    #Parameters: None
    #Gets inputs and print user interations
    #Return: None
    print('Welcome to the brazilian net calculator!')
    time.sleep(1)
    name = str(input("How you want to be called? "))
    while True:
        try:
            print('1 - Show history')
            print('2 - New calculation')
            choose = int(input('Please, choose one option:  '))
            break
        except ValueError:
            print("Please enter a valid number.")
    if choose == int(1):
        stored_name = input('What is your stored name? *case sensitive ')
        history = show_history(stored_name)
        if history.empty:
            print(f'User {stored_name} not found.')
        else:
            print(history)
        
    elif choose == int(2):
        while True:
            try:
                gross_salary = float(input("Enter your gross salary: "))
                num_dependents = int(input("Enter the number of dependents: "))
                alimony = float(input("Enter the alimony value: "))
                break
            except ValueError:
                print("Please enter a valid number. Use just numbers and dot if needed.")
        inss_discount = inss(gross_salary)
        irrf_discount = irrf(gross_salary, num_dependents, alimony)
        net_salary = gross_salary - inss_discount - irrf_discount
        gross_salary = f'{gross_salary:.2f}'
        inss_discount = f'{inss_discount:.2f}'
        irrf_discount = f'{irrf_discount:.2f}'
        net_salary = f'{net_salary:.2f}'
        print(f"Gross Salary: {gross_salary}")
        print(f"INSS Discount: {inss_discount}")
        print(f"IRRF Discount: {irrf_discount}")
        print(f"Net Salary: {net_salary}")
        now = datetime.now()
        month = now.strftime('%B')
        date = now.strftime('%Y-%m-%d %H:%M:%S')
        history_input = [name, date, month, gross_salary, inss_discount, irrf_discount, net_salary ]
        while True:
            try:
                save_history = str(input("Do you want to save this calculation into the history file? YES(y) / NO(n)  "))
                break
            except ValueError:
                print("Please enter just Yes(y) or No(n).")
        if save_history.lower() == 'yes' or save_history.lower() == 'y':
            save_history_file(history_input)
            print('Thank you for using the brazilian net calculator!!')
        else:
            print('Thank you for using the brazilian net calculator!!')
def save_history_file(history_input):
    #Parameters: The list of all date to be inserted to the csv file
    #Write the current calculation into the history file.
    #Return: None
    with open('history.csv', mode='a', newline='') as csv_file:
                writer= csv.writer(csv_file)
                writer.writerow(history_input)

def show_history(name):
    #Parameters: Name
    #read the csv and returns the data frame filtered by name.
    #Return: A dataframe
    df = pd.read_csv('history.csv')
    user_history = df[(df['Name'] == name)]
    return user_history
def inss(gross_salary):
    #Parameters: Gross salary
    #Calculate the INSS discount based on the gross salary
    #Return: discounted salary
    if gross_salary <= 1320.00:
        deduction = gross_salary * 0.075
    elif gross_salary <= 2571.29:
        deduction = gross_salary * 0.09 - 19.80
    elif gross_salary <= 3856.94:
        deduction = gross_salary * 0.12 - 96.94
    elif gross_salary <= 7507.49:
        deduction = gross_salary * 0.14 - 174.08
    else:
        deduction = 876.95 

    return deduction if deduction < gross_salary else gross_salary


def irrf(gross_salary, num_dependents, alimony):
    #Parameters: Gross salary, numbers of dependents and alimony of every month
    #Calculate the IRRF discount based on the gross salary
    #Return: discounted salary
    # INSS deduction
    inss_deduction = inss(gross_salary)

    # IRRF calculation base
    irrf_base = gross_salary - inss_deduction - (num_dependents * 189.59) - alimony

    # IRRF Table
    if irrf_base <= 2112.00:
        irrf_deduction = 0
    elif irrf_base <= 2826.65:
        irrf_deduction = irrf_base * 0.075 - 158.40
    elif irrf_base <= 3751.05:
        irrf_deduction = irrf_base * 0.15 - 370.40
    elif irrf_base <= 4664.68:
        irrf_deduction = irrf_base * 0.225 - 651.73
    else:
        irrf_deduction = irrf_base * 0.275 - 884.96

    return irrf_deduction if irrf_deduction > 0 else 0

if __name__ == "__main__":
    main()