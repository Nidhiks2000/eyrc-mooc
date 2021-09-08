#!/bin/bash

#take the input file name which is passed as an argument
args=("$@")
#find the number of lines with one or more digits present in the input file
var=$(cat $1 | grep -w "\b[[:digit:]]*\b"  | wc -l)
#print the number of line with one or more digits found
printf "Number of lines having one or more digits are: $var\n"
printf "Digits found:\n"
#find the digivarts present in the input file
grep -o "\b[[:digit:]]*\b" $1
#print the digits found

