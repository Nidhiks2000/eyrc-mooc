#!/bin/awk -f

BEGIN{
	FS=",";
	RS="!";
	OFS="\t";
	
	
	
	
	
	
	
	printf "Value\tSensorNumber\t\n"
}
{
if(NF==2){
print $1,$2
}

}
END{

} 



