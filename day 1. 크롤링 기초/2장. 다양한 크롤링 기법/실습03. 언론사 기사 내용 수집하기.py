# from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

# elice_utils = EliceUtils()

def main():
  list_href = []
  list_content = []

  url = "https://news.sbs.co.kr/news/newsflash.do?plink=GNB&cooper=SBSNEWS"
  req = urllib.request.Request(url)
  sourcecode = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(sourcecode, "html.parser")

  # find_all을 사용한 이유는 찾아야 하는 항목이 여러 개 였음
  for href in soup.find_all("div", class_="mfn_inner"):
    list_href.append("https://news.sbs.co.kr" + href.find("a")["href"])
      
  # 리스트 url 하나하나씩 실행    
  for i in range(0, len(list_href)) :
    url = list_href[i]
    req = urllib.request.Request(url)
    sourcecode = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(sourcecode, "html.parser")
    
    # 여기서는 찾아야 하는 항목이 하나니까 find를 사용
    list_content.append(soup.find("div", class_="text_area").get_text())
  print(list_content)
if __name__ == "__main__":
  main()