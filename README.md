# Election_Analysis

## Overview

The purpose of this project was to audit the results of a local election across three counties (Arapahoe, Jefferson, and Denver). Looking at 368,991 lines of data for unique votes, this project is able to confirm voter turnout and the election winner. 

## Election-Audit Results:

- There were 368,991 votes cast in this congressional election. 
- Please see the below breakdown of voter turnout percentage and total count of votes: 

Jefferson: 10.5% (38,855)\n
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

- As evidenced above, Denver county had the largest number of votes with 306,055 ballots cast. 
- Please see below a breakdown of the number of votes and the percentage of the total votes each candidate received:

Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

From this, we can see that the clear winner of this election was Diana DeGette with 272,892 votes making up 73.8% of votes cast. 

## Election-Audit Summary

I would like to propose to the election committee that we could alter the Python code used in this analysis to apply to any election moving forward. We could add a position field to the csv file and another "for" loop to the code for pull the winning candidate for each position (e.g. senator, commissioner, etc) listed on
the ballot. We can also add analysis for statewide results so that after listing the county voter turnout percentage and total votes, we can provide the same information at the state level to provide a complete picture of the election data. 
