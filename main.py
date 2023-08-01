from pathlib import Path
import csv

from cash_on_hand import calculate_CashOnHand_difference
from profit_loss import calculate_netProfit_difference

cash_fp = Path.cwd() / "csv_report" / "Cash_on_Hand.csv"
with cash_fp.open(mode="r", encoding="UTF-8", newline="") as cash_file:
    cash_reader = csv.reader(cash_file)
    next(cash_reader)  # skip header

    cash_on_hand = []
    for row in cash_reader:
        cash_on_hand.append([row[0], int(row[1])])


highest_cash_surplus, highest_cash_surplus_day, cash_deficits = calculate_CashOnHand_difference(cash_on_hand)
def print_cash_surplus(highest_cash_surplus, highest_cash_surplus_day):
    """
    - This function formats and prints the results according to the format in the print statement 
    - Parameter required: highest_cash_surplus
    """
    print("[CASH SURPLUS]: CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    print(f"[HIGHEST CASH SURPLUS]: DAY: {highest_cash_surplus_day}, AMOUNT: USD{highest_cash_surplus}")
def print_cash_deficit(cash_deficits):
    """
    - This function formats and prints the results according to the format in the print statement 
    - Parameter required: cash_deficits
    """
    for day, deficit in cash_deficits:
        print(f"[CASH DEFICIT] DAY: {day}, AMOUNT: USD{abs(deficit)}")
        # abs is used to ensure that all the values are positive
if cash_deficits:
    print_cash_deficit(cash_deficits)
# if there are no cash deficits where it keeps profitting, it will only print cash surplus and the day
elif highest_cash_surplus > 0:
    print_cash_surplus(highest_cash_surplus, highest_cash_surplus_day)


profit_fp = Path.cwd() / "csv_report" / "Profits_and_loss.csv"
with profit_fp.open(mode="r", encoding="UTF-8", newline="") as profit_file:
    profit_reader = csv.reader(profit_file)
    next(profit_reader)  # skip header

    profitLoss = []
    for row in profit_reader:
        profitLoss.append([row[0], int(row[4])])

highest_profit_increase, highest_profit_increase_day, profit_loss = calculate_netProfit_difference(profitLoss)
def print_profit_surplus(highest_profit_increase, highest_profit_increase_day):
    """
    - This function prints the highest profit increase and its corresponding day
    - Parameter required: highest_profit_increase, highest_profit_increase_day
    """
    print(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN PREVIOUS DAY")
    print(f"[HIGHEST NET PROFIT SURPLUS] DAY: {highest_profit_increase_day}, AMOUNT: USD{highest_profit_increase}")

def print_profit_deficit(profit_loss):
    """
    - This function prints the profit deficit amount and its corresponding day
    - Parameter required: profit_loss
    """
    for day, values in profit_loss:
        print(f"[PROFIT DEFICIT] DAY: {day}, AMOUNT: USD{abs(values)}")

highest_profit_increase, highest_profit_increase_day, profit_loss = calculate_netProfit_difference(profitLoss)

# If there are profit loss days, print the loss and days.
if profit_loss:
    print_profit_deficit(profit_loss)
# Else, print the highest net profit increase.
else:
    print_profit_surplus(highest_profit_increase, highest_profit_increase_day)