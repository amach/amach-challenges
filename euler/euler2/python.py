#!/usr/bin/env python

# Iterative summation of even fibonacci numbers (up to a given n)
def sum_even_fib(n):
    sum = 0
    num1 = 1
    num2 = 2

    while(num2 < n):
        if(num2 % 2 == 0):
            sum += num2

        temp = num1
        num1 = num2
        num2 = temp + num1

    return sum

def main():
    print sum_even_fib(4000000)

if __name__ == '__main__':
    main()
