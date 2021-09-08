#!/bin/sed -f


# write the sed command to remove single-line and multi-line comments
# but not delete those line
#s/\/\*.*\*\///g
 #s|/\*|\n&|g;s|*/|&\n|g
# /\/\*/,/*\//d
#:loop
#s|\(.*\)/\*.*\*/|\1|
#t loop
#/\/\*/!b
#N
#b loop
:loop
s|\(.*\)\/\*.*\*\/|\1|
s|\/\/.*||g
t loop
# /\/\*/!b 
N
b loop




