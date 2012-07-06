#!/usr/bin/env python

def palin(st):
  return st.lower() == st[::-1].lower()

def main():
  
  st = raw_input('Enter your potential palindrome: ')

  if palin(st):
    print st + ' is a palindrome!'
  else:
    print st + ' is not a palindrome!'

if __name__ == '__main__':
  main()
