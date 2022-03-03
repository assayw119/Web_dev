from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# name이 bobby인 데이터 삭제
db.users.delete_one({'name':'bobby'})