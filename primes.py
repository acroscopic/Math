# This is a script to generate prime numbers as you guess them. Can you get to 100?

import math
import os

os.system('cls' if os.name == 'nt' else 'clear') # clears the screen

def primes(n):
	if n == 1:
		return False # 1 is not prime
	if n == 2:
		return True # 2 is prime 
	if n > 2 and n % 2 == 0:
		return False # even numbers are not prime

	max_divisor = math.floor(math.sqrt(n)) # setting up square roots
	for d in range(3, 1 + max_divisor, 2): # you only need to check if prime up to the square root 
		if n % d == 0:
			return False 
	return True # if it meets all the requirements, it's prime. 

count = 1
while(True):
	for n in range(1, 2147483647): # 2147483647 is the max 32bit int, I couldn't get floats to work
		if(primes(n) == True): # only show the prime numbers
			guess = int(input(f"What is prime number {count}? "))
			if(str(guess)) == str(0):
				os.system('cls' if os.name == 'nt' else 'clear')
				print(f"Prime number {count} is {n}")
				count = 1
				break
			if(str(guess)) == str(n):
				print(f"\033[FWhat is prime number {count}? {n} is correct!")
				count += 1
			else:
				os.system('cls' if os.name == 'nt' else 'clear')
				print(f"Try again. Prime numer {count} is {n}")
				count = 1
				break
