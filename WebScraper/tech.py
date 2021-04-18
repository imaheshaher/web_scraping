import csv

dict = [
    ["1",'mahesh',"aher"],
    ["2","sagar","shelke"],
    ["3","om","namo"]
]

fname = "tech.csv"

with open(fname,"w+") as f:
    writer = csv.writer(f)
    writer.writerows(dict)


with open(fname,"r") as f:
    for i in f:
        print(i.split(","))
        