#!/bin/bash

echo -n "What is your name? "
read -e NAME
echo -n "How old are you? "
read -e AGE
echo -n "What is your reddit username? "
read -e USERNAME

STR="Your name is $NAME, you are $AGE years old, and your username is $USERNAME"

echo $STR
echo $STR > bash_output.txt
