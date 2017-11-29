import csv

with open("budget_data_1.csv",newline = "") as budgetdata1:
    data1_reader = csv.reader(budgetdata1, delimiter = ",")
    with open("budget_data_2.csv", newline ="")as budgetdata2:
        data2_reader = csv.reader(budgetdata2, delimiter = ",")
        with open("budget_data.csv", 'a', newline = "") as budget_data:
            writer = csv.writer(budget_data, delimiter = ",")
            for row in data1_reader:
                writer.writerow(row)
            header = next(data2_reader)
            for row2 in data2_reader:
                writer.writerow(row2)

    
