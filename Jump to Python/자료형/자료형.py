# 본 파일은 Python 학습자료에서 배운 내용을 복습하는 공간입니다. 
# 학습자료에서 나온 예시를 먼저 구현하고 예시를 바탕으로 변형하여 실습하였습니다. 
# 예시 코드는 "#" 로 표시하였고 그 외에는 학습을 바탕으로 복습한 변형 코드입니다. 
# 출처 : 점프 투 파이썬 (박응용, 위키독스) https://wikidocs.net/12

# 1. 자료형
# a = 3
# b = 4
# print(a + b),(a - b),(a * b),(a / b),(a ** b),(a % b),(b % a)

a = 12
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** b)

print(12 % 4)
print(4 % 12)
print(a % b)
print(b % a)

# a = 1
# a = a + 1
# print(a)

c = 3
c = c + 3
print(c)

# a = 1
# a -= 1 (+=, -=, *=, /=, //=, %=, **=)
# print(a)

d = 3
d += 3
d -= 3
d *= 3
d /= 3
d //= 3
d %= 3
d **= 3 
print(d)