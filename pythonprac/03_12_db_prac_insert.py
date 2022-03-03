from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta # 'dbsparta'를 이름으로 하는 DB에 접근, 없으면 자동 생성

# 기억해야 할 것 : insert / find / update / delete

doc = {'name':'bobby','age':21}
db.users.insert_one(doc) # 'user'라는 Collections 안에 insert

db.users.insert_one({'name':'kay','age':27})
db.users.insert_one({'name':'john','age':30})