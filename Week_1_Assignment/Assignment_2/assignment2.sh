#!/bin/bash

#take the input of csv file name which is passed as an argument

args=("$@")
#print complete details only if the first column data is starting with letter "R"
#and sort it alphabetically based on first column data
 grep "^R" $1 | sort 


