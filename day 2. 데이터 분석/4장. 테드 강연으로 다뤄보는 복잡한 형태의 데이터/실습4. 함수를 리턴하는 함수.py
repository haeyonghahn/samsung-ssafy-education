# 만약 age_validator = min_validator(0)이 있으면
# 0보다 작거나 다른 문자열이 들어오면 false를 리턴해주는 함수를 만들 것임
def min_validator(minimum):
  '''
  주어진 값이 정수가 아니거나 최솟값 minimum보다 작으면 False를 리턴하는 함수를 리턴합니다.
  '''
  def helper(n):
    # n의 타입이 정수가 아니면 False를 리턴합니다.
    if type(n) is not int:
      return False
    # 아래 함수를 완성하세요.
    if minimum <= n :
      return True
    else :
      return False
  return helper
    
'''
만약 나이가 이상한 값인지 확인하기 위해서 
age_validator라는 함수를 만들 것이다.
"age_validator = min_validator(0)"
나이의 최솟값이 0이라는 age_validator라는 함수를 만들었다.

근데 ,만약에 age_validator(-1)이라는 숫자가 들어왔는데
이것이 나이가 될 수 있는 숫자인지 물어보면, false를 반환할 것이다.

이러한 함수를 만들 것이 age_validator
'''     
    
# 예를 들어, age_validator = max_validator(100)이 있으면
# 100보다 크거나 다른 문자열이 들어오면 false를 만드는 함수를 만들 것임
def max_validator(maximum):
  '''
  주어진 값이 정수가 아니거나 최댓값 maximum보다 크면 False를 리턴하는 함수를 리턴합니다.
  '''   
  def helper(n):
    # n의 타입이 정수가 아니면 False를 리턴합니다.
    if type(n) is not int :
      return False
    # 아래 함수를 완성하세요.
    if maximum < n :
      return False
    else :
      return True
  return helper


def validate(n, validators):
  # validator 중 하나라도 통과하지 못하면 False를 리턴합니다.
  for validator in validators:
    if not validator(n):
      return False
  
  return True


# 작성한 함수를 테스트합니다. # 아래 주석을 해제하고 결과 값을 확인해보세요.
# # 나이 데이터를 검증하는 validator를 선언합니다. 
age_validators = [min_validator(0), max_validator(120)]
ages = [9, -3, 7, 33, 18, 1999, 287, 0, 13]

# # 주어진 나이 데이터들에 대한 검증 결과를 출력합니다.
print("검증 결과")
for age in ages:
  result = "유효함" if validate(age, age_validators) else "유효하지 않음"
  print("{}세 : {}".format(age, result))
