# One Text read time estimator:

## User Story:
As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## Function Signature:
- Function should count the length of the string in words and tell how long it should 
take to read
- Parameters: Should take a string to estimate the time of reading.
- Returns: Should return a time taken to read the string in seconds

## Examples:
- Given a string of 100 words, the function should return 30 seconds.
- Given a string of 50 words, the function should return 15 seconds.
- Given a string of 200 words, the function should return 60 seconds.