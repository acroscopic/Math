# I wrote this script to test supercomputer run times

import sys
import time

def lucas_lehmer(p, result_file):
    # Performs the Lucas-Lehmer test for Mersenne primes
    if p < 2:
        return False
    s = 4
    m = (1 << p) - 1  # Equivalent to 2**p - 1
    print(f"Testing Mersenne number for 2^{p} - 1")

    for i in range(p - 2):
        s = (s * s - 2) % m
    is_prime = s == 0
    # Write the final result to the result file
    result_message = f"Mersenne prime test for 2^{p} - 1: {'Prime' if is_prime else 'Not Prime'}\n"
    result_file.write(result_message)
    result_file.flush()  # Ensure immediate writing to result file
    return is_prime

# Given Mersenne number exponent
p = 2282

# p = 136279841 is the largest known prime as of 2025
# Using this value is not feasible for this program, it would require like 500gb of memory or something crazy


# Open result file for final result
result_file_path = "lucas_lehmer_result.txt"

start_time = time.time()

with open(result_file_path, "a") as result_file:
    # Run the Lucas-Lehmer test
    is_prime = lucas_lehmer(p, result_file)

end_time = time.time()

elapsed_time = end_time - start_time
elapsed_time_message = f"Elapsed time: {elapsed_time:.2f} seconds\n"
print(elapsed_time_message, end='')

with open(result_file_path, "a") as result_file:
    result_file.write(elapsed_time_message)
    result_file.flush()  # Ensure immediate writing to result file
