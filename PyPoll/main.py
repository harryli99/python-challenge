import csv

file_input = "election_data.csv"
file_output = "election_analysis.txt"

total_votes = 0
candidate_list = []
candidate_votes = []
vote_count = []
percent_vote = []

with open(file_input) as elecData:
    csvreader = csv.DictReader(elecData)
    for row in csvreader:
        total_votes += 1
        candidate_votes.append(row["Candidate"])
        if (row["Candidate"] not in candidate_list):
            candidate_list.append(row["Candidate"])
           
         
for i in range(len(candidate_list)):
    vote_count.append(candidate_votes.count(candidate_list[i]))
       
for j in range(len(vote_count)):
    percent_vote.append(vote_count[j]/total_votes)

Winner = candidate_list[vote_count.index(max(vote_count))]

with open(file_output, 'w') as txt_file:

    elect_result = (f"\nElection Results\n"
                    f"------------------------\n"
                    f"Total Votes: {total_votes}\n"
                    f"------------------------\n")
    print(elect_result, end="")
    txt_file.write(elect_result)
    for k in range(len(candidate_list)):
        votes_output = f"{candidate_list[k]}: {percent_vote[k]*100:.3f}% ({vote_count[k]})\n"
        print(votes_output, end="")
        txt_file.write(votes_output)

    winner_output = (f"-------------------------\n"
                      f"Winner: {Winner}\n"
                      f"-------------------------\n")
    print(winner_output)

    txt_file.write(winner_output)
    
        


        
                          
