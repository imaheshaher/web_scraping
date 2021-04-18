import requests
from bs4 import BeautifulSoup
import csv


url = "http://districts.nic.in/stateut.php"

data = requests.get(url)

soup = BeautifulSoup(data.content,'html5lib')
file_name="state_record1.csv"


state_data =[]
district_link=[]
def get_data():
    d= soup.find_all('div',attrs={'class':'stateabbr'})
    return d

def get_state():
    d= get_data()
    for i in d:
        for j in i.ul:
            state = j.a.text
            district = j.a['href']
            # print(district)
            district_link.append(district)
            state_data.append(state)
    

def state_file():
    with open(file_name,'w+') as csvfile:
        for s in state_data:
            csvfile.write(s)
            csvfile.write('\n')

def get_district_link():
    get_state()
    return district_link
if __name__ == '__main__':
    get_state()
    
    state_file()