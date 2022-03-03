from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# name이 bobby인 데이터에서 age를 19로 변경
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 여러 개의 같은 값을 변경하고 싶은 경우 update_many를 사용