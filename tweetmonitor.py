#!/usr/bin/python
from TwitPerson import TwitPerson
import time
import sys

if len(sys.argv) < 2:
    print('Please enter a valid twitter handle.\n')
    sys.exit(0)
else:
    twit_id = sys.argv[1]
print(' Press Ctrl+C to terminated.\n')
person = TwitPerson(twit_id)

rest_interval = 600
person.display_tweets()
time.sleep(rest_interval)
while True:
    person.new_tweets()
    time.sleep(rest_interval)