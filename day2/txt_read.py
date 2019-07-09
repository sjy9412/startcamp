# window - cp949 (encoding)
# mac/web... - utf-8

# with open('ssafy_with.txt', 'r') as f:
#     print(f.read())

with open('ssafy_with.txt', 'r') as f:
    # readlines는 라인을 각각 리스트의 원소로 반환한다.
    lines = f.readlines()

# strip : 앞뒤의 공백(개행문자)를 없애 준다.
for line in lines:
    print(line.strip())

with open('ssafy.txt', 'r') as f:
    # read : 전체 내용을 하나의 string으로 반환한다.
    txt = f.read()

print(txt)
print(type(txt))