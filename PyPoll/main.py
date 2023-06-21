#dependencies 
import os
import csv

# Files to load and output
CSV_PATH = os.path.join('Resources', 'election_data.csv')
OUTPUT_PATH = os.path.join('analysis', 'election_data.txt')
total_votes = 0
candidate_list = []
candidate_votes = {}
winner_votes = 0 
winner = ""

with open(CSV_PATH) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)
    total_votes = 0
    
    for row in csv_reader:
        total_votes += 1
        if (row[2] not in candidate_list):
            candidate_list.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] += 1
txt_file_results = ( 
f"Election Results\n"
f"--------------------\n"
f"Total Votes: {total_votes}\n"
f"------------------------------\n"
)
print(txt_file_results)


with open(OUTPUT_PATH, "w") as textfile:

    textfile.write(txt_file_results)
    for candidate in candidate_votes:
        
        print(candidate)
        #textfile.write(f"{candidate} ")

        votes = candidate_votes[candidate]
        print(votes)
        # textfile.write(f"({votes})\n")

        percent_votes = float(votes)/float(total_votes) * 100
        print(percent_votes)
        # textfile.write(f"{percent_votes:.3f}%\n")
        
        textfile.write(f"{candidate} ")
        textfile.write(f"{percent_votes:.3f}% ")
        textfile.write(f"({votes})\n")

        if (votes > winner_votes): 
            winner_votes = votes
            winner = candidate
        winner_candidate= (
        f"---------------------------------\n"
        f"Winner: {winner}\n")
    textfile.write(winner_candidate)
print(winner_candidate)

        # candidate_finals = (
        # f"{candidate}: {percent_votes:.3f}% ({votes})\n"
        # f"{candidate_list[1]}: {percent_votes:.3f}% ({votes})\n"
        # f"{candidate_list[2]}: {percent_votes:.3f}% ({votes})\n")
        # print(candidate_finals)
        # textfile.write(candidate_finals)

        



# output = (
# f"Election Results\n"
# f"--------------------\n"
# f"Total Votes: {total_votes}\n"
# f"--------------------------------\n"
# f"{candidate_list[0]}: {percent_votes:.3f}% ({votes})\n"  
# f"{candidate_list[1]}: {percent_votes:.3f}% ({votes})\n"
# f"{candidate_list[2]}: {percent_votes:.3f}% ({votes})\n"
# f"---------------------------------\n"
# f"Winner: {winner}\n"
# f"---------------------------------\n"
# )

# print(output)

# with open(OUTPUT_PATH, "w") as output_file:
#     output_file.write()
    


