#The data we need to retrieve
# Assign a variable for the file to load and the path.
import csv
import os

file_to_load = os.path.join("..","Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# Open the election results and read the file
     ##Can someone tell me why we effectively have two variables (file to load and election data) for the one election csv?
with open(file_to_load) as election_data:

# To do: read and analyze data here 
     file_reader = csv.reader(election_data)
     headers = next(file_reader)
     print(headers) 

     for row in file_reader: 
          print(row)

#1. The total number of votes cast 

#2. A complete list of candidates who received votes 

#3. The percentage of votes each candidate won 

#4. The total number of votes each candidate won 

#5. The winner of the election based on popular vote 

# Close the file.
#election_data.close()





