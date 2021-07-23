# for문을 무작정 따라해보기
for i  in range(1,11):
    if (i%2 == 0):
        print(i, "은/는 짝수입니다.")
    else:    
        print(i,"은/는 홀수입니다")

#for 문의 구조
# for i in 범위:
#   반복할 명령어1
#   반복할 명령어2

#for 문 with List
mylist = ['해달이','사스미','메기']
for i in mylist:
    print(i)
print("반복문 끝")

# print list with range
print(list(range(10))) # 시작점 기본값은 0!
print(list(range(1,11))) #step 기본값은 1
print(list(range(1,20,3)))
print(list(range(20,0,-3)))

#for문 with range
for i in range(1,11):
    print(i,end=" ")
print('반복 끝')