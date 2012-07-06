#!/usr/bin/env python

def palin(st):
  
  # remove non-alphanumeric chars from the string
  alphanum_st = ''.join(c for c in st if c.isalnum())

  # convert to lowercase
  alphanum_st = alphanum_st.lower()

  # compare the string to its reverse
  return alphanum_st == alphanum_st[::-1]

def main():
  
  st = raw_input('Enter your potential palindrome: ')

  if palin(st):
    print '"' + st + '" is a palindrome!'
  else:
    print '"' + st + '" is not a palindrome!'

if __name__ == '__main__':
  main()
