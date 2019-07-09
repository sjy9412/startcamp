# number.txt를 읽어서
# 리스트 (readlines)

with open('number.txt','r') as f:
    numbers = f.readlines()

# 리스트를 뒤집는다.
numbers.reverse

# number_reverse.txt로 저장
with open('number2.txt','w') as file:
    for number in numbers:
        file.write(number)

# Alt + 방향키 하면 해당하는 줄이 이동함. 