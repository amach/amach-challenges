#!/usr/bin/env python

def main():

  # range() excludes the upper bound; 1-100 is range(1, 101)
  for num in range(1, 101):
    if num % 15 == 0:
      print 'FizzBuzz'
    elif num % 3 == 0:
      print 'Fizz'
    elif num % 5 == 0:
      print 'Buzz'
    else:
      print num

# boilerplate to call main() function
if __name__ == '__main__':
  main()
