# from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

# elice_utils = EliceUtils()


def main():
  list_pagination = []
  
  for i in range(0, 5) :
    # 첫 번째 페이지 url = http://sports.donga.com/Enter?p=1&c=02
    # 두 번째 페이지 url = http://sports.donga.com/Enter?p=21&c=02
    # 세 번째 페이지 url = http://sports.donga.com/Enter?p=41&c=02
    url = "http://sports.donga.com/Enter?p=" + str((i*20) + 1) + "&c=02"
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")

    # range(10) [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # 기사 갯 수: 17개 
    for i in range(3, 20) :
      list_pagination.append((soup.find_all("span", class_="tit")[i].get_text()))
  print(list_pagination)

if __name__ == "__main__":
  main()