from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")
db=client["office"]
coll=db["workers"]


idn=input("Enter id: ")
nm=input("empnm: ")
dnm=input("dept: ")
p=input("post: ")
cty=input("city: ")
sal=input("salary: ")
mob=input("moblie: ")
em=input("email: ")
coll.insert_one({"_id":idn,"empnm":nm,"dept":dnm,"post":p,"city":cty,"salary":sal,"mobile":mob,"email":em})

print("worker details inserted")