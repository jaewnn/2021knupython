#시험 점수에 따른 과락 분류 2
score = int(input('점수를 입력하세요 '))
if score >= 70:
    result = '통과'
elif score >= 60:
    result = '재시험'
else:
    result = '과락'
print(result)