import os
import csv

cvs_path = os.path.join("..", "budget_data.csv")
with open(cvs_path) as csvfile:
    csvreader = csv.reader(csvfile)

    print(csvreader)


    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

    for row in csvreader:
         print(row)
