"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
# score = {
#     '수학': 80,
#     '국어': 90,
#     '음악': 100
# }

# # 아래에 코드를 작성해 주세요.
# result = sum(score.values())/len(score)
# print(result)





# # # 2. 반 평균을 구하시오. -> 전체 평균
# scores = {
#     'a': {
#         '수학': 80,
#         '국어': 90,
#         '음악': 100
#     },
#     'b': {
#         '수학': 80,
#         '국어': 90,
#         '음악': 100
#     }
# }

# # 아래에 코드를 작성해 주세요.
# total = []
# for score in scores.values():
#     result = sum(score.values())/len(score)
#     total.append(result)
# print(sum(total)/len(scores))





# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
average = {}
for key in city:
    average[key] = sum(city[key])/len(city[key])

for key, value in average.items():
    print('%s : %.2f' %(key,value))
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""


# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
city_name = [name for name in city.keys()]
result = [avg for avg in average.values()]
max_city = (max(result))
min_city = (min(result))
print('가장 더웠던 곳:',city_name[result.index(max_city)])
print('가장 추웠던 곳:',city_name[result.index(min_city)])



# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
for i in city['서울']:
    if i == 2:
        result1 = '있음'
        break
    else:
        result1 = '없음'

print(result1)