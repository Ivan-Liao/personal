from faker import Faker
import json

# creates json file
output=open('data1.json','w')
fake=Faker()
alldata={}
alldata['records']=[]
for x in range(1000):
	data={"name":fake.name(),"age":fake.random_int(min=18, max=80, step=1),"street":fake.street_address(),"city":fake.city(),"state":fake.state(),"zip":fake.zipcode(),"lng":float(fake.longitude()),"lat":float(fake.latitude())}
	alldata['records'].append(data)	
json.dump(alldata,output)

# reads the json file we created
with open("data1.json","r") as f:
	data=json.load(f)
print(type(data))
print(data['records'][0]['name'])
