import random
import shelve
import os
from timeit import default_timer as timer

os.system('cls' if os.name == 'nt' else 'clear') #Clearing the screen

#making a high score system
filename = "score"
if not os.path.exists(filename):
    s = shelve.open(filename)
    s['score'] = 0
    s.close()
count = 0


while(True):
	twodigit = random.randint(10, 99)
	print(f"11 x {twodigit}?") # what is 11 times random 2 digit number
	start = timer()
	answer = int(input())
	end = timer()
	time = int(end) - int(start) # calculates time it take to do the problem
	
	if answer == (11*twodigit):
		print("Correct!")
		print(f"{time} seconds!")
		count = count + 1
	else:
		print("Incorrect!")
		break

s = shelve.open(filename)
current = s['score']

if current >= count:
    print("Your high score is: " + str(current))

if current < count:
    highscore = count
    print("Your new high score is: " + str(highscore))
    s['score'] = count


s.close()