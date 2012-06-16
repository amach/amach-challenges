# This program finds, and prints, the sum of all multiples of 3 or 5 below 1000.

import sys

# Returns the sum of all multiples of 3 or 5 up to a given limit
def sum_mult35(limit):
    sum = 0

    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            sum += i

    return sum

def main():
    print sum_mult35(1000)

if __name__ == '__main__':
    main()
