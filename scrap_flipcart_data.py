import requests
from bs4 import BeautifulSoup
import csv
import re

url="https://www.flipkart.com/mobile-phones-store"

r=requests.get(url)

soup=BeautifulSoup(r.content,"html5lib")
name=[]
price=[]
filename="mobiledata128.csv"
f=csv.writer(open(filename,"w",encoding="utf-8"))
f.writerow(["name" , "Price" ])

#class="tcb-post-content tcb-shortcode thrv_wrapper"
for data in soup.findAll('a',attrs={'class':'K6IBc-'}):
    n=data.find('div',attrs={'class':'iUmrbN'})
    p=data.find('div',attrs={'class':'M_qL-C'})
    if  None in (n,p):
        continue

    
    name.append(n.text)
    price.append(p.text.strip())


    f.writerow([n.text , p.text.strip("₹")])
   

print(name)
print(price)