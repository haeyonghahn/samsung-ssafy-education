# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
import re

# 031 - 123 -2345
# 010 - 234 -2345
# 이런 형태의 데이터만 추출해서 가공하는 것을 실습
def main():
  sentence = "제보는 032-232-3245 또는 010-222-2233 으로 연락주시기 바랍니다."
  print(sentence)

  compile_text = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
  # 만약에 compile(r'010-\d\d\d-\d\d\d\d) 이라면,
  match_text = compile_text.findall(sentence)
  print(match_text)

  #----------------------------------------------------------------------
  
  email = ["aa2@naver.com", "kbc@aaaaa", "Alice@Alice.com", "ILove@CodingLove"]

  compile_text = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

  for i in email:
    print(i)
    # 이메일 양식이 지켜진다면 true를 출력
    print(compile_text.match(i) != None)

    print("-------------")

if __name__ == "__main__":
  main()