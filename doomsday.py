

#This program was made to practice John Conway's Doomsday Algorithim (https://en.wikipedia.org/wiki/Doomsday_rule) 
#It loops random dates, and only breaks the loop when an attempt is failed. It also features a simple high score tracker, and a timer.


import shelve
import random
import calendar
import os
from timeit import default_timer as timer


#Creating the high score file if it does not already exist
filename = "score"
if not os.path.exists(filename):
    s = shelve.open(filename)
    s['score'] = 0
    s.close()
count = 0

os.system('cls' if os.name == 'nt' else 'clear')

while(True):

    #Generating random dates
    year = random.randint(1583, 3000)
    months = [None, 31, 28, 31, 30, 31, 30, 30, 31, 30, 31, 30, 31]
    month = random.randint(1, 12)
    day = random.randint(1, months[month])

    print(str(month) + "/" +  str(day) + "/" + str(year)) #date to guess
    weekday = (calendar.weekday(year, month, day) + 1) #correct answer
    start = timer() # starts the timer
    attempt = input("Calculate the day of the week of this date:") #input answer
    # input needs to be 0-6: 0 = Sun 1 = Mon 2 = Tues 3 = Wed 4 = Thur 5 = Fri 6 = Sat
    end = timer() # ends the timer
    time = int(end) - int(start) # calculates time it take to do the problem



    if int(attempt) == weekday:
        print("Success!")
        print(f"{time} seconds!")
        count = count + 1

    if int(attempt) != weekday:
        break

count = count - 1


s = shelve.open(filename)
current = s['score']

if current >= count:
    print("Your high score is: " + str(current))

if current < count:
    highscore = count
    print("Your new high score is: " + str(highscore))
    s['score'] = count
    
s.close()
