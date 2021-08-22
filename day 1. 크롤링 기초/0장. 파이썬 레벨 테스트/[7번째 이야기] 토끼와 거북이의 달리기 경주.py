def gcb(a, b) :
  while(b != 0) :
    temp = a % b
    a = b
    b = temp
  return abs(a)
    
def lcm(a, b) :
  gcb_value = gcb(a, b)
  if(gcb_value == 0) :
    return 0
  return abs((a * b) / gcb_value)

N, M = input().split() # 입력값을 한 개의 input으로 받아야함
number1 = int(N)
number2 = int(M)
result = lcm(number1, number2)
print(int(result))