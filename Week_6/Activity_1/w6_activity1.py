
# No other modules apart from 'argparse', 'os' and 'datetime' need to be imported
# as they aren't required to solve the assignment

# Import required module/s
import argparse
import os
from datetime import datetime


def executePwdCmd(args):
	"""Execute the `pwd` shell command in the directory from where this file is called to run.

	Parameters
	----------
	args : Namespace
		Arguments passed when 'pwd' command is called
	
	Example
	-------
	$ python3 w6_activity1.py pwd

	/home/erts-09/Desktop/SFC_PartI_MOOC
	"""
	
	##############	ADD YOUR CODE HERE	##############
	
	
	print(os.getcwd())

	##################################################


def executeDateCmd(args):
	"""Execute the `date` shell command to print the current date in format: "Tuesday 11 May 2021".

	Parameters
	----------
	args : Namespace
		Arguments passed when 'date' command is called
	
	Example
	-------
	$ python3 w6_activity1.py date

	Tuesday 11 May 2021
	"""

	##############	ADD YOUR CODE HERE	##############
	today = datetime.now()
	days = ["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
	months = ["None","January","February","March","April","May","June","August","September","October","November","December"]
	day = days[today.weekday()]
	month = months[today.month]
	res = [day,str(today.day),month,str(today.year)]
	str1 = " " 
    
    # return string  
	print(str1.join(res))
	

	##################################################


def executeCatCmd(args):
	"""Execute the `cat` shell command to print the contents of file(s) passed as positional arguments to the standard output.

	Parameters
	----------
	args : Namespace
		Arguments passed when 'cat' command is called
	
	Example
	-------
	$ python3 w6_activity1.py cat file_name

	< contents of file for the given file_name >

	=======

	$ python3 w6_activity1.py cat file1_name file2_name

	< contents of file for the given file1_name >
	< contents of file for the given file2_name >

	=======

	$ python3 w6_activity1.py cat file_name
	
	cat: file_name: No such file or directory
	
	< if the given file_name does not exist at the given file path >

	=======

	$ python3 w6_activity1.py cat dir_name
	
	cat: dir_name: Is a directory
	
	< if the dir_name is an existing directory then print the appropriate message >
	"""

	##############	ADD YOUR CODE HERE	#############
	
	for i in args.file:
		
		if(os.path.isdir(i)):
			print("cat: {}: Is a directory".format(i))
			
		elif(os.path.isfile(i)==False):
			print("cat: {}: No such file or directory".format(i))
			
		else:
			with open(i) as file:
				for line in (file.readlines()):
					print(line,end="")

					
	##################################################


def executeHeadCmd(args):
	"""Execute the `head` shell command to print the first 10 LINES of a file passed as positional arguments to the standard output
	OR print only the first NUM LINES of a file if optional argument 'n' or 'lines' is passed.
	Print the name of file as header as well if optional argument 'v' or 'verbose' is passed.

	Parameters
	----------
	args : Namespace 
		Arguments passed when 'head' command is called
	
	Example
	-------
	$ python3 w6_activity1.py head file_name

	< contents of first 10 lines for the given file_name >

	=======

	$ python3 w6_activity1.py head file_name -n 3

	< contents of first 3 lines for the given file_name >

	=======

	$ python3 w6_activity1.py head file_name -n 3 -v
	
	==> file_name <==
	< contents of first 3 lines for the given file_name >

	=======

	$ python3 w6_activity1.py head file_name
	
	head: cannot open 'file_name' for reading: No such file or directory
	
	< if the given file_name does not exist at the given file path >

	=======

	$ python3 w6_activity1.py head dir_name
	
	head: error reading 'dir_name': Is a directory
	
	< if the dir_name is an existing directory then print the appropriate message >
	"""
	
	##############	ADD YOUR CODE HERE	##############

	i = args.file
	if(os.path.isdir(i)):
		print("head: error reading '{}': Is a directory".format(i))
		exit()
	elif(os.path.isfile(i)==False):
		print("head: cannot open '{}' for reading: No such file or directory".format(i))
		exit()

	else:
			
		if args.lines:

			if args.verbose:

			
				print("==>",i,"<==")
				a_file = open(i)
				for i in range(args.lines):
					line = a_file.readline()
					print(line,end = "")
			else:
				a_file = open(i)
				for i in range(args.lines):
					line = a_file.readline()
					print(line,end = "")

		else:
			a_file = open(i)
			for i in range(10):
				line = a_file.readline()
				print(line,end = "")


	##################################################


def executeTailCmd(args):
	"""Execute the `tail` shell command to print the last 10 LINES of a file passed as positional arguments to the standard output
	OR print only the last NUM LINES of a file if optional argument 'n' or 'lines' is passed.
	Print the name of file as header as well if optional argument 'v' or 'verbose' is passed.

	Parameters
	----------
	args : Namespace
		Arguments passed when 'tail' command is called
	
	Example
	-------
	$ python3 w6_activity1.py tail file_name

	< contents of last 10 lines for the given file_name >

	=======

	$ python3 w6_activity1.py tail file_name -n 3

	< contents of last 3 lines for the given file_name >

	=======

	$ python3 w6_activity1.py tail file_name -n 3 -v
	
	==> file_name <==
	< contents of last 3 lines for the given file_name >

	=======

	$ python3 w6_activity1.py tail file_name
	
	tail: cannot open 'file_name' for reading: No such file or directory
	
	< if the given file_name does not exist at the given file path >

	=======

	$ python3 w6_activity1.py tail dir_name
	
	tail: error reading 'dir_name': Is a directory
	
	< if the dir_name is an existing directory then print the appropriate message >
	"""
	
	##############	ADD YOUR CODE HERE	##############
	
	file1 = args.file
	
	
	
	

	if os.path.isdir(file1):
		print("tail: error reading '{0}': Is a directory".format(file1))

	elif os.path.isfile(file1) == False:
		print("tail: cannot open '{}' for reading: No such file or directory".format(file1))
	else:
	
	
		if args.lines:
			if(args.verbose == False) :#(property == "verbose") and (value == False)) :
				with open(file1) as file:
					for line in (file.readlines()[-args.lines:]):
						print(line,end = "")
						
			elif(args.verbose):
				print("==>",file1,"<==")
				with open(file1) as file:
					for line in (file.readlines()[-args.lines:]):
						print(line,end = "")		

		else:
			with open(file1) as file:
				for line in (file.readlines()[-10:]):
					print(line,end = "")		
	
	
	
	
	##################################################


def executeShellCommands():
	"""Executes Shell commands such as `pwd`, `date`, `cat`, `head` and `tail` and outputs on Terminal when called.

	Example
	-------
	$ python3 w6_activity1.py -h
	
	usage: w6_activity1.py [-h] {pwd,date,cat,head,tail} ...

	Execute Shell commands in Python

	optional arguments:
	-h, --help            show this help message and exit

	shell commands:
  	  {pwd,date,cat,head,tail}
		pwd                 print name of current/working directory
		date                display the current date
		cat                 concatenate files and print on the standard output
		head                print first 10 LINES of a file to standard output
		tail                print last 10 LINES of a file to standard output

	Week-6 Activity-1

	=======

	$ python3 w6_activity1.py pwd -h

	usage: w6_activity1.py pwd [-h]

	optional arguments:
	-h, --help  show this help message and exit

	=======

	$ python3 w6_activity1.py date -h

	usage: w6_activity1.py date [-h]

	optional arguments:
	-h, --help  show this help message and exit

	=======

	$ python3 w6_activity1.py cat -h

	usage: w6_activity1.py cat [-h] file [file ...]a_file = open(file1)
					lines = a_file.readlines()
					last_lines=lines[-args.lines:]
					#print(last_lines)
					line=''.join(last_lines)
					print(line,end = "")

	positional arguments:
	file        path of file(s) to output contents on standard output

	optional arguments:
	-h, --help  show this help message and exit

	=======

	$ python3 w6_activity1.py head -h

	usage: w6_activity1.py head [-h] [-n NUM] [-v] file

	positional arguments:
	file                 path of file to output contents on standard output

	optional arguments:
	-h, --help           show this help message and exit
	-n NUM, --lines NUM  print the first NUM lines instead of the first 10
	-v, --verbose        always output headers giving file names

	=======

	$ python3 w6_activity1.py tail -h

	usage: w6_activity1.py tail [-h] [-n NUM] [-v] file

	positional arguments:
	file                 path of file to output contents on standard output

	optional arguments:
	-h, --help           show this help message and exit
	-n NUM, --lines NUM  print the last NUM lines instead of the last 10
	-v, --verbose        always output headers giving file names

	"""

	##############	ADD YOUR CODE HERE	##############
	
	

	parser = argparse.ArgumentParser(allow_abbrev=False,description="Execute Shell commands in Python",epilog="Week-6 Activity-1")
	#parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(title = 'shell commands')
	parser_pwd = subparsers.add_parser('pwd',help = 'print name of current/working directory')
	parser_pwd.set_defaults(func=executePwdCmd)
	parser_date = subparsers.add_parser('date', help = 'display the current date')
	parser_date.set_defaults(func=executeDateCmd)
	parser_cat = subparsers.add_parser('cat',help="concatenate files and print on the standard output")
	
	file1=parser_cat.add_argument("file", help="path of file(s) to output contents on standard output",nargs="+")
	parser_cat.set_defaults(func=executeCatCmd)
	
	parser_head = subparsers.add_parser('head', help = 'print first 10 LINES of a file to standard output')
	parser_head.set_defaults(func=executeHeadCmd)
	parser_head.add_argument("-n","--lines",help="print the first NUM lines instead of the first 10",metavar = "NUM",type = int)
	parser_head.add_argument("-v", "--verbose",help="always output headers giving file names",action = "store_true")
	parser_head.add_argument("file", help="path of file to output contents on standard output",metavar="file")
	
	parser_tail = subparsers.add_parser('tail', help = 'print last 10 LINES of a file to standard output')
	parser_tail.set_defaults(func=executeTailCmd)
	parser_tail.add_argument("-n","--lines",help="print the last NUM lines instead of the last 10",metavar = "NUM",type = int)
	parser_tail.add_argument("-v","--verbose",help="always output headers giving file names",action = "store_true")
	parser_tail.add_argument("file", help="path of file to output contents on standard output",metavar = "file")
	
	
	args = parser.parse_args()
	args.func(parser.parse_args())
	
	
	
	
	
	
	
	
	

	

	##################################################


if __name__ == "__main__":
	"""Main function, code begins here
	"""
	executeShellCommands()
