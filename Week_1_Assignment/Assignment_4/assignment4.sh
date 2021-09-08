#!/bin/bash
args=("$@")
x=${args[0]}
y=${args[1]}

r()
{

	square_root=`echo "sqrt(($x*$x)+($y*$y))" | bc -l`
	printf "%.5f, " $square_root
}

atan ()
{
    degree=`echo "a($y/$x)*180.00000/3.14159265358979328" | bc -l`
	
}

if [ $x -gt 0 ] && [ $y -gt 0 ];then
	r
	atan
	printf "%.5f\n" $degree
elif [ $x -lt 0 ] && [ $y -gt 0 ];then
	r 
	atan
	theta=`echo "$degree+180" | bc -l`
	printf "%.5f\n" $theta
elif [ $x -lt 0 ] && [ $y -lt 0 ];then
	r 
	atan
	theta=`echo "$degree+180" | bc -l`
	printf "%.5f\n" $theta
elif [ $x -gt 0 ] && [ $y -lt 0 ];then
	r 
	atan
	theta=`echo "$degree+360" | bc -l`
	printf "%.5f\n" $theta 
elif [ $x -eq 0 ] && [ $y -eq 0 ];then
	rad1=0.00000
	teta1=0.00000
	printf "$rad1, $teta1\n"

elif [ $x -gt 0 ] && [ $y -eq 0 ];then
	rad2=$x
	teta2=0.00000
	printf "%.5f, " $rad2
	printf "$teta2\n"
elif [ $x -lt 0 ] && [ $y -eq 0 ];then
	rad3=`echo "$x*-1" | bc -l`
	teta3=180.00000
	printf "%.5f, " $rad3
	printf "$teta3\n"
elif [ $x -eq 0 ] && [ $y -gt 0 ];then
	rad4=$y
	teta4=90.00000
	printf "%.5f, " $rad4
	printf "$teta4\n"
elif [ $x -eq 0 ] && [ $y -lt 0 ];then
	rad5=`echo "$y*-1" | bc -l`
	teta5=270.00000
	printf "%.5f, " $rad5
	printf "$teta5\n"

fi

