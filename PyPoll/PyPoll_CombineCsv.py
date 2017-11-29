import csv

with open("election_data_1.csv",newline = "") as electiondata1:
    data1_reader = csv.reader(electiondata1, delimiter = ",")
    with open("election_data_2.csv", newline ="")as electiondata2:
        data2_reader = csv.reader(electiondata2, delimiter = ",")
        with open("election_data.csv", 'a', newline = "") as election_data:
            writer = csv.writer(election_data, delimiter = ",")
            for row in data1_reader:
                writer.writerow(row)
            header = next(data2_reader)
            for row2 in data2_reader:
                writer.writerow(row2)

    
