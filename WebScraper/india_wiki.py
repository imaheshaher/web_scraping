import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_districts_in_India"
r=requests.get(url)

soup = BeautifulSoup(r.content,'html5lib')
a=[]
d=soup.find('table',{'class':"wikitable sortable"})
a= d.find_all('td')[2::]
for i in a:
    print(i.text)

