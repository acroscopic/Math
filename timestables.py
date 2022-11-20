# Practice times tables up to 14, or higher with simple modification.

import random
from timeit import default_timer as timer
import os

os.system('cls' if os.name == 'nt' else 'clear') #Clearing the screen

count = 0

while(True):
	int1 = random.randint(0,14) #picks 2 random numbers
	int2 = random.randint(1,14)

	answer = (int1 * int2) # multiplies 2 numbers
	start = timer()
	guess = input(f'{int1} * {int2} = ')
	end = timer()
	time = int(end) - int(start) # calculates time it take to do the problem
	if(int(guess)) == (int(answer)):
		print(f"Correct! {time} seconds!")
		count = count + 1
	else:
		print("Incorrect!")
		print(f'{int1} * {int2} = {answer}\n')
		break

print("Your score is: " + str(count))
