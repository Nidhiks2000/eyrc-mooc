
# Import required module/s
import socket
from prettytable import PrettyTable
import ast

# NOTE: You are free to use any module(s) required for better representation of the data received from the Server.

# NOTE: DO NOT modify the connectToServer() and the 'if' conditions in main() function.
# 		Although you can make modifications to main() where you wish to call formatRecvdData() function.

def connectToServer(HOST, PORT):
	"""Create a socket connection with the Server and connect to it.

	Parameters
	----------
	HOST : str
		IP address of Host or Server, the Client needs to connect to
	PORT : int
		Port address of Host or Server, the Client needs to connect to

	Returns
	-------
	socket
		Object of socket class for connecting and communication to Server
	"""

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.connect((HOST, PORT))
	server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

	return server_socket


def formatRecvdData(data_recvd):
	"""Format the data received from the Server as required for better representation.

	Parameters
	----------
	data_recvd : str
		Data received from the Server about scheduling of Vaccination Appointment
	"""

	##############	ADD YOUR CODE HERE	##############
	
	x = PrettyTable()
		
	dict2 = eval(data_recvd)
		
	x.field_names=["OPTION_NUMBER","OPTIONS","ADDITIONAL INFO"]
	for key,value in dict2.items():
		value = str(value)
		if '{' in value:
				d = eval(value)
				for i,j in d.items():

					x.add_row([key,i,j])
				
		else:
				
			x.add_row([key,value,"-"])
	print(x)
	

	##################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	print('--------------------------------------------------------------------------------')
	print('                         WELCOME TO COWIN CHATBOT                               ')
	print('--------------------------------------------------------------------------------')
	# Define constants for IP and Port address of the Server to connect to.
	# NOTE: DO NOT modify the values of these two constants
	HOST = '127.0.0.1'
	PORT = 24680

	# Start the connection to the Server
	server_socket = None
	try:
		server_socket = connectToServer(HOST, PORT)
	except ConnectionRefusedError:
		print("*** Start the server first! ***")
	
	# Receive the data sent by the Server and provide inputs when asked for.
	if server_socket != None:
		while True:
			data_recvd = server_socket.recv(1024).decode('utf-8')
			

			if '>>>' in data_recvd:
				if '{' in data_recvd:
					input_data = data_recvd.split("\n")
					print(input_data[0])
					
					formatRecvdData(input_data[1])
					data_to_server = input()
					server_socket.sendall(data_to_server.encode('utf-8')) 
				else:
					print(data_recvd)
					
					data_to_send = input()
				
					server_socket.sendall(data_to_send.encode('utf-8'))
					
			else:
				print(data_recvd,"\n")
			
			
			if not data_recvd:
				server_socket.close()
				break
		
		server_socket.close()
