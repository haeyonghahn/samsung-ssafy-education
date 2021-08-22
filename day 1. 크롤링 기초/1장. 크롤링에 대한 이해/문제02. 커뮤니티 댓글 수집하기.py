# from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

# elice_utils = EliceUtils()

def main():
  print("커뮤니티 댓글")

  # 댓글를 수집할 사이트 주소 입력
  url = "https://pann.nate.com/talk/344083297"

  # URL 주소에 있는 HTML 코드를 soup에 저장합니다.
  soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
  #print(soup)

  list = []
  
  # 1. 댓글이 있는 태크 dd 찾기
  # 2. class_="usertxt class 찾기"
  # for 반복문과 get_text()를 사용해서 출력
  dd = soup.find_all("dd", class_="usertxt")
  for i in dd :
    list.append(i.find("span").get_text().strip())    
  #print(list)
  
  # N = " 안녕하세요 한해용 입니다. "
  # print(N.strip("다. "))
    
if __name__ == "__main__":
  main()