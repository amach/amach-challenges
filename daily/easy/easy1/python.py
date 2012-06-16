#!/usr/bin/python

import sys

def main():
    
    f = open('python_output.txt', 'w')

    name = raw_input('What is your name? ')
    age = raw_input('What is your age? ')
    username = raw_input('What is your reddit username? ')

    st = 'Your name is {0}, you are {1} years old, and your username is {2}\n'.format(name, age, username)

    print st
    f.write(st)

    f.close()
    
if __name__ == '__main__':
    main()
