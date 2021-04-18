import csv
dict = {'Andaman and Nicobar Island (UT)': 5, 'Andhra Pradesh': 13, 'Arunachal Pradesh': 25, 'Assam': 33, 'Bihar': 38, 'Chandigarh (UT)': 13, 'Chhattisgarh': 27, 'Dadra and Nagar Haveli (UT)': 13, 'Daman and Diu (UT)': 14, 'Delhi (NCT)': 11, 'Goa': 3, 'Gujarat': 33, 'Haryana': 22, 'Himachal Pradesh': 12, 'Jammu and Kashmir(UT)': 20, 'Jharkhand': 24, 'Karnataka': 30, 'Kerala': 14, 'Ladakh(UT)': 10, 'Lakshadweep (UT)': 8, 'Madhya Pradesh': 51, 'Maharashtra': 36, 'Manipur': 16, 'Meghalaya': 11, 'Mizoram': 8, 'Nagaland': 11, 'Odisha': 30, 'Puducherry (UT)': 7, 'Punjab': 22, 'Rajasthan': 33, 'Sikkim': 4, 'Tamil Nadu': 37, 'Telangana': 31, 'Tripura': 8, 'Uttarakhand': 13, 'Uttar Pradesh': 75, 'West Bengal': 23}
sum =0
k=dict.keys()
print(len(k))
for i,j in dict.items():
    sum=sum+j

print(sum)

fname = "no_of_district.csv"

with open(fname,'w+') as f:
    writer = csv.writer(f)
    for i,j in dict.items():
        f.write(i)
        f.write('-')
        f.write(str(j))
        f.write("\n")
