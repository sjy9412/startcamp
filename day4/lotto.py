import random
import pprint
import requests
url="https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
# 1. 요청 (json은 딕셔너리)
# json -> 파이썬의 dictionary와 list로 변환하여 조작할 수 있다.
# 응답 (HTML, XML, JSON)
response = requests.get(url).json()
# pprint.pprint(response)


# print(f'내가 선택한 번호는 {my_lotto}입니다.')
# count = 0

# for num in [f'drwtNo{i}' for i in range(1,7)]:
#     if response[num] in my_lotto:
#         count += 1

# if count == 6:
#     result = '1등'
# elif count == 5 and response['bnusNo'] in my_lotto:
#     result = '2등'
# elif count == 5:
#     result = '3등'
# elif count == 4:
#     result = '4등'
# elif count == 3:
#     result = '5등'
# else:
#     result = '해당 없음'

# print(f'6개 중에 {count}개 맞았습니다. 결과는 {result}입니다.')

result = [0, 0, 0, 0, 0]
win_lotto = []
for i in range(1,7):
    win_lotto.append(response[f'drwtNo{i}'])
bonus = response['bnusNo']

for i in range(10000000):

    my_lotto = random.sample(range(1,46), 6)

    # matched = 0
    # for num in my_lotto:
    #     if num in win_lotto:
    #         matched += 1

    # 교집합의 개수를 구한다.
    matched = len(set(win_lotto) & set(my_lotto))

    if matched == 6:
        result[0] += 1
    elif matched == 5 and bonus in my_lotto:
        result[1] += 1
    elif matched == 5:
        result[2] += 1
    elif matched == 4:
        result[3] += 1
    elif matched == 3:
        result[4] += 1
    print(result, end='\r')

print('끝')
print(result)