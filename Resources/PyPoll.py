#The data we need to retrieve
# Assign a variable for the file to load and the path.
import csv
import os

file_to_load = os.path.join("..","Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

total_votes = 0 
candidate_options = []
candidate_votes = {}
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
     ##Can someone tell me why we effectively have two variables (file to load and election data) for the one election csv?
with open(file_to_load) as election_data:

# To do: read and analyze data here 
     file_reader = csv.reader(election_data)
     headers = next(file_reader)    

     for row in file_reader: 
          #1. The total number of votes cast 
          total_votes += 1 
          #2. A complete list of candidates who received votes 
          candidate_name = row[2]
          if candidate_name not in candidate_options:
               candidate_options.append(candidate_name)
               candidate_votes[candidate_name]=0
     
          candidate_votes[candidate_name]+=1
     with open(file_to_save, "w") as txt_file:
          election_results = (
               f"\nElection Results\n"
               f"--------------------\n"
               f"Total Votes = {total_votes:,}\n"
               f"--------------------\n")

          print(election_results, end="")
          txt_file.write(election_results)

          #3. The percentage of votes each candidate won 
          for candidate_name in candidate_votes:
               votes = candidate_votes[candidate_name]
               vote_percent = float(votes)/float(total_votes) * 100 
               #print(f"{candidate_name} received {vote_percent:.1f}% of the vote\n")

               #4. The total number of votes each candidate won 
               if (votes > winning_count) and (vote_percent > winning_percentage):
                    winning_count = votes
                    winning_percentage = vote_percent
                    winning_candidate = candidate_name

               candidate_results = (f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
               print(candidate_results)
               txt_file.write(candidate_results)
          #5. The winner of the election based on popular vote 
          winning_candidate_summary = (
               f"--------------------------\n"
               f"Winner: {winning_candidate}\n"
               f"Winning Vote Count: {winning_count:,}\n"
               f"Winning Percentage:{winning_percentage:.1f}%\n"
               f"---------------------------\n")
          print(winning_candidate_summary)
          txt_file.write(winning_candidate_summary)


# Close the file.
#election_data.close()





