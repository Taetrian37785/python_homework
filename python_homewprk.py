import os
import csv
total_months= 0
total_net = 0
month_of_change= []  
net_change_list= []
#Empty brackets  to setup lists 
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]
#Large Range to determine min and max
cvs_path = os.path.join("budget_data.csv")
with open(cvs_path) as csvfile:
    csvreader = csv.reader(csvfile)

    csv_header = next(csvreader)
    txt_path = os.path.join("Budget Information.txt")
    textfile = open(txt_path, 'w+', newline="")
   # print(f"CSV Header: {csv_header}")
    first_row = next(csvreader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])


    for row in csvreader:
        total_months +=1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change

        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change
#If statements to help organize the min and max as well as attack the date. Help from Monali Patel in tutoring services. 
net_monthly_avg = sum(net_change_list) / len(net_change_list)
output = (
    f"Financial Analysis \n"
    f"--------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change:$ {net_monthly_avg:.2f}\n"
    f"Greatest Incease in Profits: {greatest_increase[0]}(${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})\n"
  )
textfile.write(output)
print(output)
textfile.close()

  

    
    







  
