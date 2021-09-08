#!/bin/bash

#take the input of csv file name which is passed as an argument
args=("$@")

#print the details of only 1st and 3rd column, if the first column data starts with letter "S"
#and sort it alphabetically based on first column data
sort -t"," -k1,1 --stable $1| grep "^S"|cut -d ',' -f 1,3
