# This checks if Mersenne numbers are prime by the Lucas Lehrer test.
# I wrote this program to check run times on a supercomputer

import sys
import time

def lucas_lehmer(p, result_file):
    # Performs the Lucas-Lehmer test for Mersenne primes
    if p < 2:
        return False
    s = 4
    m = (1 << p) - 1  # Equivalent to 2**p - 1

    for i in range(p - 2):
        s = (s * s - 2) % m
        if i % 10 == 0:  # Print at least every 10 iterations

    is_prime = s == 0
    # Write the final result to the result file
    result_message = f"Mersenne prime test for 2^{p} - 1: {'Prime' if is_prime else 'Not Prime'}\n"
    result_file.write(result_message)
    result_file.flush()  # Ensure immediate writing to result file
    return is_prime

# Given Mersenne number exponent
# 2^136279841 - 1 Largest known prime number as of 2025
p = 19937 # A reasonable but not too large Mersenne exponent for debugging

# Open result file for final result
result_file_path = "lucas_lehmer_result.txt"

start_time = time.time()

with open(result_file_path, "a") as result_file:
    print(f"Starting Lucas-Lehmer test for Mersenne prime 2^{p} - 1...\n")
    is_prime = lucas_lehmer(p, result_file)

end_time = time.time()

elapsed_time = end_time - start_time
elapsed_time_message = (f"Elapsed time: {elapsed_time:.2f} seconds\n")
print(elapsed_time_message)

# Write the elapsed time to the result file
with open(result_file_path, "a") as result_file:
    result_file.write(elapsed_time_message)
    result_file.flush()  # Ensure immediate writing to result file
