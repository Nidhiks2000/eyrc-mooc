#!/bin/bash

#take the input file name which is passed as an argument
args=("$@")
#find the valid IP addresses present in the input file
grep -oE "\s[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+\s" $1 | sed -E 's/^[[:space:]]+//'| awk 'BEGIN{FS="."; RS="\n" ;OFS=".";}{if(NF==4){if($1>=0 && $1<=127 && $2>=0 && $2<=255 && $3>=0 && $3<=255 && $4>=0 && $4<=255){print $1,$2,$3,$4 "A"}if($1>=128 && $1<=191 && $2>=0 && $2<=255 && $3>=0 && $3<=255 && $4>=0 && $4<=255){print $1,$2,$3,$4 "B"}if($1>=192 && $1<=223 && $2>=0 && $2<=255 && $3>=0 && $3<=255 && $4>=0 && $4<=255){print $1,$2,$3,$4 "C"}if($1>=224 && $1<=239 && $2>=0 && $2<=255 && $3>=0 && $3<=255 && $4>=0 && $4<=255){print $1,$2,$3,$4 "D"}if($1>=240 && $1<=247 && $2>=0 && $2<=255 && $3>=0 && $3<=255 && $4>=0 && $4<=255){print $1,$2,$3,$4 "E"}if($1>=248 && $1<=255 && $2>=0 && $2<=255 && $3>=0 && $3<=255 && $4>=0 && $4<=255){print $1,$2,$3,$4 "Not Defined"}}}'

#print the valid IP addresses found
 