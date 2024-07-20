import os
import csv

csvpath = os.path.join('Resources-attempt-2', 'election_data.csv')

total_votes = 0
candidate_votes = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    # print(f"CSV Header: {csvheader}")

    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]

        if candidate not in candidate_votes:
            candidate_votes[candidate] = 0
        candidate_votes[candidate] = candidate_votes[candidate] + 1

results = []
winner = ""
max_votes = 0

for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")

    if votes > max_votes:
        max_votes = votes
        winner = candidate

analysis = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    f"{''.join(results)}"
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

txtpath = os.path.join('analysis-attempt-2', 'election_results.txt')

with open(txtpath, mode='w') as txtfile:
    txtfile.write(analysis)

print(f"PyPoll analysis and results have been written to {txtpath}")
print(analysis)

