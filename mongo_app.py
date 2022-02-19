#Reference:https://github.com/vishwasbeede/Mongo-API-data

import json
import urllib3
import pymongo



#Our api access link address
http = urllib3.PoolManager() 
url = "https://api.coingecko.com/api/v3/exchange_rates"


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" This specific script grabs data from a currency database API and save it to DB: CURRENCYDATABASE and to collection: Currencyvalues")

try:
    response = http.request('GET', url)
    APIdata = json.loads(response.data)
    fp = open('coingecko.json','w', encoding='utf-8')
    fp.write(str(APIdata))
    fp.close()
    
except:
    print ("There is an error you need to solve it to keep going")

#Here is how to connect MongoDB 

Cl = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# Here we are creating a database
CurreDB = Cl["CURRENCYDATABASE"]  

# Here we are creating a database
Colomn = CurreDB["Currencyvalues"]
print("These are these databases in DB:")
print(Cl.list_database_names())

#Here how is dropping a DB

Colomn.drop()

#Here is how to insert json data into DB
xx=Colomn.insert_one(APIdata)

#Display the insert_id generated after transaction
print("Data has been inserted into DB _id: %s"%(xx.inserted_id))


#This below section is designed to call some queries to receive a response from MongoDB
#Query 1 
#List all the data from DB

def find_alldata():
    for p in Colomn.find():
        print(p)

#Query 2 
#Here there is a function to get specific values 
def find_val():
    query = { "rates.btc.name": "Bitcoin" }
    mydoc = Colomn.find(query,{"rates.btc.name":1,"rates.btc.value":1,"rates.btc.unit":1,"rates.btc.type":1})
    for p1 in mydoc:
        print(p1)
    
#Here is displaying data that are about DB to BTC currency.

find_val()

def func_parameter_data(parameter):
   
    query1 = { }

    req_val =  {"rates.cur.name":1,"rates.cur.value":1,"rates.cur.unit":1,"rates.cur.type":1}
    print(type(req_val))
    for k,v in req_val.items():
        req_val
  
    mydocument = Colomn.find(query1, { k.replace('cur', parameter): v for k, v in req_val.items() }) 
    for I in mydocument:
        print(I)

#Binance Coin
func_parameter_data("bnb")
# Bitdepositary (BDT)
func_parameter_data("bdt")
#Ethereum coin
func_parameter_data("eth")
# Indian rupee
func_parameter_data("inr")


print("-----------------------------------------------------------------------------------------------------------")

