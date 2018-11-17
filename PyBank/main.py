import os
import csv

financial_analysis_df = os.path.join("Resources" , "budget_data.csv")
with open(financial_analysis_df, 'r') as csvfile:

csvreader = csv.reader(csvfile, delimiter=",")



next(reader, None)

total_months = ("Date").count()

total_pnl = ["Profit/Losses"].sum()

avg_change = ["Profit/Losses"].stdev()

increase = ["Profits/Losses"]

decrease = ["Profits/Losses"]

print(("Total Months: ") + total_months
    ("Total Profit: ") + total_pnl
    ("Average Change: ") + avg_change
    ("Greatest Increase: ") + increase +
    ("Greatest Decrease: "))


