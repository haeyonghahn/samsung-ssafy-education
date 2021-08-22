# from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

# elice_utils = EliceUtils()

def main():
  print("href 출력해보기")

  # 하이퍼 링크를 모아두는 리스트
  list_href = []
  
  url = "http://sports.donga.com/Enter"
  soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
  #print(soup)

  #for i in soup.find_all("span", class_="tit") :
      #print(i.find("a")["href"])
  # 반복문을 사용해 원하는 정보 range(3,23)까지 find("a")["href"] 를 사용해서
  
  for i in range(3, 20) :
    # href 모두 수집하여 list_href에 저장
    list_href.append(soup.find_all("span", class_="tit")[i].find("a")["href"])
  print(list_href)

if __name__ == "__main__":
  main()