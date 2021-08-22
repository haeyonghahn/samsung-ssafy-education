# from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

# elice_utils = EliceUtils()

def main():
    
  print("네이버 인기검색어")
  # URL 데이터를 가져올 사이트 url 입력
  url = "http://www.naver.com"
      
  # URL 주소에 있는 HTML 코드를 soup에 저장합니다.
  soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
  # print(soup)
  list = []
  
  for naver_text in soup.find_all("span", class_= "ah_k") :
    list.append(naver_text.get_text())
  print(list)    
    
if __name__ == "__main__":
  main()
