
from pathlib import Path
import csv

# create a file to csv file.
fp = Path.cwd()/"csv_report"/"Profits_and_loss.csv"

# read the csv file to append day and net profit from the csv.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty lists to store day and net profit
    profitLoss=[] 

    # append day and net profit into the profitLoss list
    for row in reader:
        #get the day and net profit each day record
        #and append the profitLoss list
        profitLoss.append([row[0],int(row[4])])


def calculate_netProfit_difference(profitLoss):
    """
    - This function will calculate the difference in net profit and store the highest profit increase and its corresponding day. 
    - As well as the list of profit loss days and the differences.
    - Parameter required: profitLoss
    """
    highest_profit_increase = 0
    highest_profit_increase_day = ()
    profit_loss = []

    # iterating through the datas in the profitLoss list to calculate the difference in net profit and find the profit loss days
    for values in range (1, len(profitLoss)):
        current_net_profit = profitLoss[values][1]
        previous_net_profit = profitLoss[values-1][1]
        difference = current_net_profit - previous_net_profit

        # check for the highest profit increase
        if difference > highest_profit_increase:
            highest_profit_increase = difference
            highest_profit_increase_day = profitLoss[values][0]

        # check for the profit loss days and amount, and store them in the profit_loss list
        if current_net_profit < previous_net_profit:
            profit_loss.append((profitLoss[values][0], difference))

    return highest_profit_increase, highest_profit_increase_day, profit_loss

# def print_profit_surplus(highest_profit_increase, highest_profit_increase_day):
#     """
#     - This function prints the highest profit increase and its corresponding day
#     - Parameter required: highest_profit_increase, highest_profit_increase_day
#     """
#     print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
#     print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_profit_increase_day}, AMOUNT: USD{highest_profit_increase}")

# def print_profit_deficit(profit_loss):
#     """
#     - This function prints the profit deficit amount and its corresponding day
#     - Parameter required: profit_loss
#     """
#     for day, values in profit_loss:
#         print(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{abs(values)}")

# highest_profit_increase, highest_profit_increase_day, profit_loss = calculate_netProfit_difference(profitLoss)

# # If there are profit loss days, print the loss and days.
# if profit_loss:
#     print_profit_deficit(profit_loss)
# # Else, print the highest net profit increase.
# else:
#     print_profit_surplus(highest_profit_increase, highest_profit_increase_day)

