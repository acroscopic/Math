import random
import operator
from timeit import default_timer as timer
import os

os.system('cls' if os.name == 'nt' else 'clear') #Clearing the screen

#making a high score system

count = 0

while(True):	
	int1 = random.randint(100,999) #picks 2 random numbers
	int2 = random.randint(100,999)
	operations = random.choice([operator.add, operator.sub]) #decides whether to add or subtract
	if operations ==  (operator.add): #giving the operations string values
		operation = ("+")
	else:
		operation = ("-")
	
	answer = operations(int1,int2) # adds or subtracts the 2 numbers
	start = timer()
	guess = input(f'{int1} {operation} {int2} = ') 
	end = timer()
	time = int(end) - int(start) # calculates time it take to do the problem
	if(int(guess)) == (int(answer)):
		print(f"Correct! {time} seconds!")
		count = count + 1
	else:
		print("Incorrect!")
		print(f'{int1} {operation} {int2} = {answer}\n')
		break


    print(f"Your score is: {count}")