#Test the net salary calculator program
import net_salary_calculator as nsc
import pytest
import os
import csv


# These are the indexes of the
# elements in the periodic table.
NAME = "Bruno"
GROSS_SALARY = 4500
SAVE_HISTORY = "Yes"
NUM_DEPENDENTS = 2
ALIMONY = 0

def test_net_salary_calculator():
    """Verify if the net salary calculator works fine.
    Parameters: None
    Return: None
    """
    history_input = ['Bruno','2023-12-07 00:13:26','December','4500.00','455.92','179.34','3864.74' ]
    with open('history_copy.csv', mode='a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(history_input)
    
    check_history_file(history_input)
    # Seu código para escrever no arquivo CSV
    
    check_inss(GROSS_SALARY)
    check_irrf(GROSS_SALARY, NUM_DEPENDENTS, ALIMONY)



def check_inss(salary):

    assert nsc.inss(salary) != None , 'Not a valid INSS discounted salary.'
def check_irrf(salary, num_dependents, alimony):
    assert nsc.irrf(salary, num_dependents, alimony) != None , 'Not a valid IRRF discounted salary.'

def check_history_file(history_input):
    assert os.path.exists('history_copy.csv') and os.path.getsize('history_copy.csv') > 0, "Error writing to CSV file."
    with open('history_copy.csv', mode='r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        last_row = list(reader)[-1]
    assert last_row == history_input, "Error: Data written to CSV does not match expected data."
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
