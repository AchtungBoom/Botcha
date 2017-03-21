# Import Twitter credentials from credentials.py
import tweepy
from time import sleep
from credentials import *

# Access and authorize Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Open text file KANT.txt for reading
my_file = open('KANT.txt', 'r')
file_lines = my_file.readlines()
my_file.close()

# Create a for loop to iterate over file_lines
for line in file_lines:
    print(line)

# if statement to ensure that blank lines are skipped
    if line != '\n':
        api.update_status(line)

# else statement with pass to conclude the conditional statement
    else:
      pass

    # Add sleep method to space tweets by 5 seconds each
    sleep(3)
