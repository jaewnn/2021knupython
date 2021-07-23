# 문제 : 해달이는 1부터 100까지의 숫자르 분류하려 한다
# 리스트 "mul2"에는 2의 배수,"mul3"에는 3의 배수,"mul6"에는 6의 배수
# 나머지 수는 모두 더해서 출력하려고 한다. 해달이를 도와주자'
# 리스트,for,range,if,%,append,+=

mul2 = []
mul3 = []
mul6 = []
others = 0

for i in range(1,101):
    if i % 2 == 0:
        mul2.append(i)
    elif i % 3 == 0:
        mul3.append(i)
    else:
        others += i
for i in range(1,101):
    if i % 6 == 0:
        mul6.append(i)

print(f'mul2 : {mul2}')
print(f'mul3 : {mul3}')
print(f'mul6 : {mul6}')
print(f'others : {others}')

    