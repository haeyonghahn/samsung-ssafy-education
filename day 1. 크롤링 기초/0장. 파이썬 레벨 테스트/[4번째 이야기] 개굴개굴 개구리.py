#a = input("입력 예시")
#print(a)

a = input().split()
#print(a)

b = []

for i in a :
  b.append("개굴" * len(i))

print(' '.join(b))