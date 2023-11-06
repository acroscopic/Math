import mpmath

mpmath.mp.dps = 10

def inconsistencies():
    #Search for zeros of the Riemann Zeta function that don't lie on the critical line.
    off_critical_line = []
    n = 1 # Starting point
    while True:
        zero = mpmath.zetazero(n)  # Get the nth non-trivial zero with mpmath
        print(f"Zero #{n}: {zero}")
        if zero and not mpmath.almosteq(zero.real, 0.5, abs_eps=1e-5):
            print(f"Inconsistency found: {zero}")
            off_critical_line.append(zero)
        n += 1
    return off_critical_line

try:
    # Search for inconsistencies indefinitely
    inconsistencies = inconsistencies()

    # This part will not be reached unless the loop is broken in some other way
    if inconsistencies:
        # This line will never appear in my terminal :\
        print("\nFound inconsistencies with the Riemann Hypothesis:")
        for zero in inconsistencies:
            print(zero)

# Removes junk errors
except KeyboardInterrupt:
    print("\nStopped by user.")