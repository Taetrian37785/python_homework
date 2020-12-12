import csv
import os
csv_path = os.path.join("election_data.csv")
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
#Setting values to zero to add total values and botes
with open(csv_path) as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    txt_path = os.path.join("election results.txt")
    textfile = open(txt_path, 'w+', newline="")
    for row in reader:
#Starting loop to scroll through .csv for totaling of calues
        total_votes = total_votes + 1
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
    #Candidates isolated for vote talley. Code supplied by BCS Help 
    election_results = (
        f"\n\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    textfile.write(election_results)
    print(election_results, end="")
    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        textfile.write(voter_output)
        print(voter_output, end="")
    #Voter percentages Calculated for each candidate.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    textfile.write(winning_candidate_summary)
    print(winning_candidate_summary, end="")
    #Text neatly organized and printed to text file. 


    
   
    
    textfile.close()