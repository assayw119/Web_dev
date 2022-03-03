from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 조건에 맞는 값 find
same_ages = list(db.users.find({'age':21},{'_id':False})) # _id 컬럼은 나타내지 않음
print(same_ages)
print('*'*20)

user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)
print('*'*20)

# 전체 데이터 find
all_ages = list(db.users.find({}, {'_id':False}))
for person in all_ages:
    print(person)
print('*'*20)
