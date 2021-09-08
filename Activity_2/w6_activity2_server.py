
# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime


# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 24680


def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers.

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	req = requests.get(url_website)
	soup = BeautifulSoup(req.text, 'html.parser')
	web_page_data = soup.find_all("tr")
	web_page_data.pop(0)
	
	

	

	##################################################

	return web_page_data


def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	vaccine_doses_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	vaccine_group = []
	for th in web_page_data:
		vaccine_group.extend(th.find("td",class_="dose_num"))


	
	dict1 = sorted(set(vaccine_group))
	for i in dict1:
		vaccine_doses_dict.update({i:"Dose "+i})



	##################################################

	return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}

	##############	ADD YOUR CODE HERE	##############
	age_group = []
	for tr in web_page_data:
		tds = tr.find_all('td')
		if(tds[11].text == dose):
			age_group.append(str(tds[12].text))
	sorted_set_age_group = sorted(set(age_group))

	j = 1
	for i in sorted_set_age_group:
		age_group_dict.update({str(j):i})
		j+=1	
        

	##################################################

	return age_group_dict


def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}

	##############	ADD YOUR CODE HERE	##############
	result = []
	state_group = []
	for tr in web_page_data:
		tds = tr.find_all('td')
		if(tds[11].text == dose and tds[12].text == age_group):
			result.append(tds[1].text)
	[state_group.append(x) for x in result if x not in state_group]
	sorted_set_state_group = sorted(state_group)
	

	j = 1
	for i in sorted_set_state_group:
		states_dict.update({str(j):i})
		j+=1	
	##################################################

	return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	districts_group = []
	for tr in web_page_data:
		tds = tr.find_all('td')
		if((tds[11].text == dose and tds[12].text == age_group) and (tds[1].text) == state):
			districts_group.append(tds[2].text)
	sorted_districts_group=sorted(set(districts_group))

	j = 1
	for i in sorted_districts_group:
		districts_dict.update({str(j):i})
		j+=1	

	##################################################

	return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	#hospital_vaccine_names_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	hospital_group = []
	for tr in web_page_data:
		tds = tr.find_all('td')
		if((tds[11].text == dose and tds[12].text == age_group) and (tds[1].text) == state and tds[2].text == district):
			hospital_group.append(tds[0].text)
			hospital_group.append(tds[10].text)
			i = 1
			hospital_vaccine_names_dict = {str(i):{hospital_group[i]: hospital_group[i + 1] for i in range(0, len(hospital_group), 2)}}
			i+=1


	##################################################

	return hospital_vaccine_names_dict


def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}

	##############	ADD YOUR CODE HERE	##############
	
	vaccine_group = []
	for tr in web_page_data:
		tds = tr.find_all('td')
		if((tds[11].text == dose and tds[12].text == age_group) and (tds[1].text) == state and tds[2].text == district) and (tds[0].text == hospital_name):
			vaccine_slots = {'1':{'May 15':tds[3].text},'2':{'May 16':tds[4].text},'3':{'May 17':tds[5].text},'4':{'May 18':tds[6].text},'5':{'May 19':tds[7].text},'6':{'May 20':tds[8].text},'7':{'May 21':tds[9].text}}
			
	

	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None

	##############	ADD YOUR CODE HERE	##############

	

	s = socket.socket()         # Create a socket object
	host = '127.0.0.1'
	port = 24680 
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)             # Reserve a port for your service.
	s.bind((host, port))        # Bind to the port

	s.listen(5)                 # Now wait for client connection.
	
	client_socket, client_addr = s.accept()     # Establish connection with client.
	print ('Got connection from', client_addr)
	
	
	##################################################
	
	return client_socket, client_addr



def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	client_addr : tuple
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############
	
	client = client_conn
	web_data = web_page_data
	global no_of_attempt
	no_of_attempt = 1


	
	# Below are the functions for each state where each option is chosed from the user

	#function to recieve data from terminal
	def recieve(client_conn):
		data = client.recv(1024).decode('utf-8')
		

		return data
	#fetch vaccine slots
	def state6(client_conn,web_data):
		global vaccine_slots_selection
		global hospital_selected
		global district_selected
		global state_selected
		global age_input_vaccine
		global dose
		slot_input_message = ">>> Select one of the available slots to schedule the Appointment:"
		slot_dict = fetchVaccineSlots(web_data,hospital_selected,district_selected,state_selected,age_input_vaccine,dose)
		slot_input_message = slot_input_message+"\n"+str(slot_dict)
		client_conn.send(slot_input_message.encode())
		slot = recieve(client_conn)
		
		
		if((slot == 'b') or (slot == 'B')):
			state5(client_conn,web_data)
		elif((slot == 'q') or (slot == "Q")):
			quit_msg = "<<< See ya! Visit again :)\n"
			client_conn.send(quit_msg.encode())

			client_conn.close()
			
		else:
			if slot in slot_dict:
				slot_selected = list(slot_dict[slot].keys())[0]
				
				slot_available = slot_dict[slot][slot_selected]
				s_selected = "<<< Selected Vaccination Appointment Date: "+str(slot_selected)+"\n"
				availability = "<<< Available Slots on the selected Date: " +str(slot_available)+"\n"
				print("Vaccination Date selected: ",slot_selected)
				print("Available Slots on that date: ",slot_available)
				
				client_conn.send(s_selected.encode())
				client_conn.send(availability.encode())
				if (int(slot_available) == 0):
					slot_unavailable = '<<< Selected Appointment Date has no available slots, select another date!\n'
					client_conn.send(slot_unavailable.encode())
					state6(client_conn,web_data)
				else:
					slot_available = "<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!\n"
					exit_message = 	"<<< See ya! Visit again :)"
					client_conn.send(slot_available.encode())
					client_conn.send(exit_message.encode())
					client_conn.close()


					
			else:
				global no_of_attempt
				if (no_of_attempt == 1):
					invalid_dose_msg = "<<< Invalid input provided 1 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.send(invalid_dose_msg.encode())
					
					no_of_attempt+=1
					state6(client_conn,web_data)
					
					
				elif (no_of_attempt == 2):
					invalid_dose_msg = "<<< Invalid input provided 2 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.send(invalid_dose_msg.encode())
					
					no_of_attempt+=1
					state6(client_conn,web_data)
				elif(no_of_attempt == 3):
					invalid_dose_msg = "<<< Invalid input provided 3 time(s)! Try again.\n"
					client_conn.send(invalid_dose_msg.encode())
					print(invalid_dose_msg)
					quit_msg = "<<< See ya! Visit again :)"
					client_conn.send(quit_msg.encode())
					print("Notifying the client and closing the connection!")
					client_conn.close()

	#fetch hospital

	def state5(client_conn,web_data):
		global hospital_selected
		global district_selected
		global state_selected
		global age_input_vaccine
		global dose
		hospital_input_message = ">>> Select the Vaccination Center Name:"
		hospital_dict = fetchHospitalVaccineNames(web_data,district_selected,state_selected,age_input_vaccine,dose)
		hospital_input_message = hospital_input_message+"\n"+str(hospital_dict)+"\n"
		client_conn.send(hospital_input_message.encode())
		hospital = recieve(client_conn)
		
		
		if((hospital == 'b') or (hospital == 'B')):
			state4(client_conn,web_data)
		elif((hospital == 'q') or (hospital == "Q")):
			quit_msg = "<<< See ya! Visit again :)\n"
			client_conn.send(quit_msg.encode())

			client_conn.close()
		else:
			if hospital in hospital_dict:
				#hospitals = hospital_dict[hospital].keys()
				hospital_selected = list(hospital_dict[hospital].keys())[0]
				h_selected = "<<< Selected Vaccination Center: "+ str(hospital_selected)
				print("Selected Vaccine Center: ",str(hospital_selected))
				client_conn.send(h_selected.encode())
				state6(client_conn,web_data)
					
			else:
				global no_of_attempt
				if (no_of_attempt == 1):
					invalid_dose_msg = "<<< Invalid input provided 1 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.send(invalid_dose_msg.encode())
					
					no_of_attempt+=1
					state5(client_conn,web_data)
					
					
				elif (no_of_attempt == 2):
					invalid_dose_msg = "<<< Invalid input provided 2 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.send(invalid_dose_msg.encode())
					
					no_of_attempt+=1
					state5(client_conn,web_data)
				elif(no_of_attempt == 3):
					invalid_dose_msg = "<<< Invalid input provided 3 time(s)! Try again.\n"
					client_conn.send(invalid_dose_msg.encode())
					print(invalid_dose_msg)
					quit_msg = "<<< See ya! Visit again :)"
					client_conn.send(quit_msg.encode())
					print("Notifying the client and closing the connection!")
					client_conn.close()
	

	#fetch district	

	def state4(client_conn,web_data):
		global district_selected
		global state_selected
		global age_input_vaccine
		global dose
		district_input_message = ">>> Select the District:"
		district_dict = fetchDistricts(web_data,state_selected,age_input_vaccine,dose)
		district_input_message = district_input_message+"\n"+str(district_dict)+"\n"
		client_conn.sendall(district_input_message.encode('utf-8'))
		district = recieve(client_conn)
		
		
		if((district == 'b') or (district== 'B')):
			state3(client_conn,web_data)
		elif((district == 'q') or (district == "Q")):
			quit_msg = "<<< See ya! Visit again :)"
			client_conn.sendall(quit_msg.encode('utf-8'))

			client_conn.close()
		else:
			if district in district_dict:
				district_selected = district_dict[district]
				s_selected = "<<< Selected District: "+ str(district_selected)+"\n"
				print("District selected: ",district_selected)
				client_conn.send(s_selected.encode())
				state5(client_conn,web_data)
					
			else:
				global no_of_attempt
				if (no_of_attempt == 1):
					invalid_dose_msg = "<<< Invalid input provided 1 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.send(invalid_dose_msg.encode())
					
					no_of_attempt+=1
					state4(client_conn,web_data)
					
					
				elif (no_of_attempt == 2):
					invalid_dose_msg = "<<< Invalid input provided 2 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.send(invalid_dose_msg.encode())
					
					no_of_attempt+=1
					state4(client_conn,web_data)
				elif(no_of_attempt == 3):
					invalid_dose_msg = "<<< Invalid input provided 3 time(s)! Try again.\n"
					client_conn.send(invalid_dose_msg.encode())
					print(invalid_dose_msg)
					quit_msg = "<<< See ya! Visit again :)\n"
					client_conn.send(quit_msg.encode())
					print("Notifying the client and closing the connection!")
					client_conn.close()
	

	#fetch state	

	def state3(client_conn,web_data):
		global state_selected
		global age_input_vaccine
		global dose
		state_input_message = ">>> Select the State:"
		state_dict = fetchStates(web_data,age_input_vaccine,dose)
		state_input_message = state_input_message+"\n"+str(state_dict)+"\n"
		client_conn.send(state_input_message.encode())
		state = recieve(client_conn)
		
		
		if((state == 'b') or (state == 'B')):
			state2(client_conn,web_data)
		elif((state == 'q') or (state == "Q")):
			quit_msg = "<<< See ya! Visit again :)\n"
			client_conn.send(quit_msg.encode())

			client_conn.close()
		else:
			if state in state_dict:
				state_selected = state_dict[state]
				s_selected = "<<< Selected State: "+ str(state_selected)+"\n"
				print("State selected: ",state_selected)
				client_conn.send(s_selected.encode())
				state4(client_conn,web_data)
					
			else:
				global no_of_attempt
				if (no_of_attempt == 1):
					invalid_dose_msg = "<<< Invalid input provided 1 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.send(invalid_dose_msg.encode())
					
					no_of_attempt+=1
					state3(client_conn,web_data)
					
					
				elif (no_of_attempt == 2):
					invalid_dose_msg = "<<< Invalid input provided 2 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.send(invalid_dose_msg.encode())
					
					no_of_attempt+=1
					state3(client_conn,web_data)
				elif(no_of_attempt == 3):
					invalid_dose_msg = "<<< Invalid input provided 3 time(s)! Try again.\n"
					client_conn.send(invalid_dose_msg.encode())
					print(invalid_dose_msg)
					quit_msg = "<<< See ya! Visit again :)\n"
					client_conn.send(quit_msg.encode())
					print("Notifying the client and closing the connection!")
					client_conn.close()
	

	#fetch age group 

	def state2(client_conn,web_data):

		global age_input_vaccine 
		global dose
		age_input_message = ">>> Select the Age Group:"
		age_for_vaccination = fetchAgeGroup(web_data,dose)
		
		age_input_message = age_input_message+"\n"+str(age_for_vaccination)+"\n"
		
		client_conn.sendall(age_input_message.encode('utf-8'))
		age_input = recieve(client_conn)
		
		
		if((age_input == 'b') or (age_input == 'B')):
			state1(client_conn,web_data)
		elif((age_input == 'q') or (age_input == "Q")):
			quit_msg = "<<< See ya! Visit again :)\n"
			client_conn.sendall(quit_msg.encode('utf-8'))

			client_conn.close()
		else:
			if age_input in age_for_vaccination:
				age_input_vaccine = age_for_vaccination[age_input]
				print("Age group selected: ",age_input_vaccine)
				dose_selected = "<<< Selected Age Group: "+ str(age_for_vaccination[age_input])+"\n"
				client_conn.sendall(dose_selected.encode('utf-8'))
				state3(client_conn,web_data)
					
			else:
				global no_of_attempt
				if (no_of_attempt == 1):
					invalid_dose_msg = "<<< Invalid input provided 1 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.sendall(invalid_dose_msg.encode('utf-8'))
					
					no_of_attempt+=1
					state2(client_conn,web_data)
					
					
				elif (no_of_attempt == 2):
					invalid_dose_msg = "<<< Invalid input provided 2 time(s)! Try again.\n"
					print(invalid_dose_msg)
					client_conn.sendall(invalid_dose_msg.encode('utf-8'))
					
					no_of_attempt+=1
					state2(client_conn,web_data)
				elif(no_of_attempt == 3):
					invalid_dose_msg = "<<< Invalid input provided 3 time(s)! Try again.\n"
					client_conn.sendall(invalid_dose_msg.encode('utf-8'))
					print(invalid_dose_msg)
					quit_msg = "<<< See ya! Visit again :)\n"
					client_conn.sendall(quit_msg.encode('utf-8'))
					print("Notifying the client and closing the connection!")
					client_conn.close()
	
	# for selection of 1st dose date

	def selecting_a_date(client_conn,web_data):
		try:
			first_dose_msg = ">>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021\n"
			client_conn.sendall(first_dose_msg.encode('utf-8'))
			today = datetime.date.today()
			today_date = today.strftime("%d/%m/%Y")
			first_dose_date = recieve(client_conn)
			
			if ((first_dose_date == 'b') or (first_dose_date == 'B')):
				
				state1(client_conn,web_data)

			elif((first_dose_date == 'q' or first_dose_date == 'Q')):
				
				
				quit_msg = "<<< See ya! Visit again :)\n"
				client_conn.sendall(quit_msg.encode('utf-8'))	
			else:

				
				today_date = today_date.split("/")
				first_dose_date_list = first_dose_date.split("/")
				f_date = datetime.datetime(int(first_dose_date_list[2]),int(first_dose_date_list[1]),int(first_dose_date_list[0]))
				l_date = datetime.datetime(int(today_date[2]),int(today_date[1]),int(today_date[0]))
				delta = l_date - f_date
				no_of_weeks = delta.days//7
				
				if (no_of_weeks < 0):
					
					invalid_date_msg = "<<< Invalid Date provided of First Vaccination Dose: "+ str(first_dose_date)+"\n"
					client_conn.sendall(invalid_date_msg.encode('utf-8'))
					selecting_a_date(client_conn,web_data)
				else:

					first_dose_date_msg = "<<< Date of First Vaccination Dose provided: "+ str(first_dose_date)+"\n"
					client_conn.send(first_dose_date_msg.encode())
					no_of_weeks_message= "<<< Number of weeks from today: "+ str(no_of_weeks)+"\n"
					client_conn.send(no_of_weeks_message.encode())
					

					if(no_of_weeks >= 4) and (no_of_weeks <= 8):
						
						second_dose = "<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.\n"
						client_conn.sendall(second_dose.encode('utf-8'))
									
						state2(client_conn,web_data)
					elif(no_of_weeks > 8):
						late_time = no_of_weeks - 8
						late_time = str(late_time)
						greater_second_dose_message = "<<< You have been late in scheduling your 2nd Vaccination Dose by "+ late_time+" weeks\n"

						client_conn.sendall(greater_second_dose_message.encode('utf-8'))
						state2(client_conn,web_data)
					else:
						early_week = 4 - no_of_weeks
						invalid_second_dose_msg = "<<< You are not eligible right now for 2nd Vaccination Dose! Try after " + str(early_week)+" weeks.\n"
							
						client_conn.send(invalid_second_dose_msg.encode())
						print("Notifying the client and closing the connection!")
						quit_msg = "<<< See ya! Visit again :)\n"
						client_conn.sendall(quit_msg.encode('utf-8'))
						client_conn.close()
			

		except ValueError:
			invalid_date = "<<< Invalid Date provided of First Vaccination Dose:"+ first_dose_date+"\n"
			
			selecting_a_date(client_conn)

	#fetching the dose
	def state1(client_conn,web_data):
		global dose
		dose_input_msg = ">>> Select the Dose of Vaccination:"
		#client_conn.send(dose_input_msg.encode())	
		vaccine_doses = fetchVaccineDoses(web_page_data)
		string_vaccine_doses = dose_input_msg+"\n"+str(vaccine_doses)
		
		client_conn.send(string_vaccine_doses.encode())
		dose = recieve(client)
		
		if((dose == 'b') or (dose == 'B')):
			
			state1(client_conn,web_data)
		elif((dose == 'q') or (dose == "Q")):
			quit_msg = "<<< See ya! Visit again :)\n"
			client_conn.send(quit_msg.encode())

			client_conn.close()
		else:
			if dose in vaccine_doses:
				dose_selected = "<<< Dose selected: "+dose+"\n"
				print("Dose selected: ",dose)
				client_conn.sendall(dose_selected.encode('utf-8'))
				if (dose == '1'):
					state2(client_conn,web_data)
				elif(dose == '2'):
					selecting_a_date(client_conn,web_data)
					
			else:
				global no_of_attempt
				if (no_of_attempt == 1):
					invalid_dose_msg = "<<< Invalid input provided 1 time(s)! Try again."
					client_conn.sendall(invalid_dose_msg.encode('utf-8'))
					print(invalid_dose_msg)
					no_of_attempt+=1
					
					state1(client_conn,web_data)
				elif (no_of_attempt == 2):
					invalid_dose_msg1 = "<<< Invalid input provided 2 time(s)! Try again."
					client_conn.sendall(invalid_dose_msg1.encode('utf-8'))
					print(invalid_dose_msg1)
					no_of_attempt+=1
					state1(client_conn,web_data)
				elif(no_of_attempt == 3):
					invalid_dose_msg2 = "<<< Invalid input provided 3 time(s)! Try again."
					client_conn.sendall(invalid_dose_msg2.encode('utf-8'))
					print(invalid_dose_msg2)
					quit_msg = "<<< See ya! Visit again :)"
					client_conn.sendall(quit_msg.encode('utf-8'))
					print("Notifying the client and closing the connection!")
					client_conn.close()
	
					

	schedule_msg = "Schedule an Appointment for Vaccination:\n\n"
	client_conn.sendall(schedule_msg.encode('utf-8'))



	state1(client,web_data)
		

	


	##################################################


def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############
	
	quit_msg = "<<< See ya! Visit again :)"
	client_conn.send(quit_msg.encode())

	client_conn.close()
	

	##################################################


################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################


##############################################################


if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()
	startCommunication(client_conn, client_addr, web_page_data)
