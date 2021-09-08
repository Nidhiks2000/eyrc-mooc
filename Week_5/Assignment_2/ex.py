import requests
from bs4 import BeautifulSoup
req = requests.get('https://www.cse.iitb.ac.in/archive/page222?batch=MTech1')
soup = BeautifulSoup(req.text, 'html.parser')
link = []
str1=""
for a in soup.find_all('a',string = "NIDHI"):

    user=(a['href'])
    res=user.replace('/','')
    u=res.replace('~','')
    str1=str1+u
    print(str1)

if not str1:
    print("Full Name does not exist on website")
