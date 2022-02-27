import pymongo as pymongo

client = pymongo.MongoClient("mongodb+srv://Naveen:Naveen95@cluster0.ykocn.mongodb.net/test?retryWrites=true&w=majority")
db = client['test']
allcountries = db.countries
allcontinents = db.continents

#1.get all country by letter or word given in the name : for example FR
print("List of countries having fr in their name")
myquery = allcountries.find({"name":{"$regex":'fr',"$options":'i'}})
for i in myquery:
    print(i["name"])


#3.send the list of continent with their number of countries
print("list of continents with their number of countries ")
myquery=allcontinents.find()
for i in myquery:
    print("Continent:"+i["name"]+", Number of Countries:"+" ",len(i["countries"]))

#4.countries of continent by alphabetic order
print("\n \n countries of continent by alphabetic order\n")
result=allcontinents.find()
for i in result:
    countries=allcountries.find({"_id":{"$in":i["countries"]}}).sort("name")
    dl=[]
    for d in countries:
        dl.append(d["name"])
    print("Continent:"+i["name"]+","+"Countries"+"[",dl,"]")

#6.display Countries in ascending order of their population
print("\n \n display Countries in ascending order of their population\n")
resultCountry = allcountries.find().sort("population")

for i in resultCountry:
    print("country:"+i["name"],","+"population:",i["population"])

#7.Get countries having u in name with more than 100000
print("\n \n Get countries having u in name with more than 100000\n")
result = allcountries.find({"name":{"$regex":'u',"$options":'i' } ,"population":{'$gt':100000}})
for i in result:
    print("country:"+i["name"],","+"population:",i["population"])