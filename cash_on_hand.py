from pathlib import Path
import csv

# creating a file to csv file
fp = Path.cwd()/"csv_report"/"Cash_on_Hand.csv"

# read the csv file to append profit and quantity from the csv
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list to store time sheet and cash on hand record
    cash_on_hand = []

    # append time sheet and cash on hand record into the cash_on_hand list
    for row in reader:
        # obtain the day and cash on hand for each record 
        # and append the cash_on_hand list
        cash_on_hand.append([row[0], int(row[1])])



def calculate_CashOnHand_difference(cash_on_hand):
    """
    - This function will calculate the difference in cash on hand and store the deficits and its corresponding day
    - Parameter required: cash_on_hand
    """
    highest_cash_surplus = 0
    cash_deficits = []

    # iterating through the datas in the cash_on_hand list to calculate the difference in cash on hand  
    for value in range(1, len(cash_on_hand)):
        previous_cash_surplus = cash_on_hand[value - 1][1]
        current_cash_surplus = cash_on_hand[value][1]
        difference = current_cash_surplus - previous_cash_surplus
        
        # check if the difference of the cash on hand is increasing/ decreasing 
        if current_cash_surplus < previous_cash_surplus:
            cash_deficits.append((cash_on_hand[value][0], difference))
        
        # if the surplus of the current is cash on hand is higher than the previous
        # current surplus will be the new "highest cash surplus"
        # day of the new "highest cash surplus" will be recorded as well
        if difference > highest_cash_surplus:
            highest_cash_surplus = difference
            highest_cash_surplus_day = cash_on_hand[value][0]

    # store highest cash surplus, its day and any other cash deficits into separate variables
    return highest_cash_surplus, highest_cash_surplus_day, cash_deficits