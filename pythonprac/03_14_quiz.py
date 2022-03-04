from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 매트릭스의 평점 구하기
mat_star = db.movies.find_one({'title' : '매트릭스'})['star']
print(mat_star)
print('*'*20)

# 매트릭스의 평점과 같은 영화 제목 불러오기
movies = list(db.movies.find({'star':mat_star}))
for movie in movies:
    print(movie['title'])
print('*'*20)

# 매트릭스 평점 0으로 수정하기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
