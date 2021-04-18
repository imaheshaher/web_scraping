import state
import requests
import csv
from bs4 import BeautifulSoup
district =state.get_district_link()
cnt =1

# url = district[0]
# r= requests.get(url)
# soup = BeautifulSoup(r.content,'html5lib')
# print(soup.prettify())
# # print(r.content)
def get_district(url):
    
    r= requests.get(url)
    soup=BeautifulSoup(r.content,'html5lib')
    return soup

csv_file = "district1.csv"
dict={}
def get_data(soup):
    state_label = soup.find('h2')
    state_name = state_label.label.text
    dict[state_name]=[]
    
    with open(csv_file,"a+") as csvfile:
        csvfile.write(state_name)
        csvfile.close()
    district_data = soup.find_all('div',attrs={'class':"distabbr"})
    print("----",state_name,"---------\n")
    for i in district_data:
        
        for k in i.find_next('ul'):
            try:
                dist_name= k.a.text
                print(k.a.text)
                # list.append(dist_name)
                dict[state_name].append(dist_name)
                with open(csv_file,'a+') as csvfile:
                    csvfile.write(dist_name)
                    csvfile.write("\n")
                    csvfile.close()

                
            except:
                print("Not found")
    dict[state_name]=len(dict[state_name])




    



for url in district:
    soup=get_district(url)
    get_data(soup)
    



print(cnt)
print(dict)  

# dist_file="dist.csv"
# with open(dist_file,'w+') as csvfile:
#     for i,j in dict.items():
#         csvfile.write(i)
#     csvfile.write("\n")
#     for i,j in dict.items():
#         csvfile.write(j)
#         csvfile.write