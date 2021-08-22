# from elice_utils import EliceUtils
import urllib.request
from bs4 import BeautifulSoup

# elice_utils = EliceUtils()


def main():
    
  # URL 데이터를 가져올 사이트 url 입력
  url = "http://www.kyeonggi.com/?mod=news&act=articleList&view_type=S&sc_code=1439458030"

  # URL 주소에 있는 HTML 코드를 soup에 저장합니다.
  soup = BeautifulSoup(urllib.request.urlopen(url).read(), "html.parser")
  #print(soup)
  
  list_title = []
  list_summary = []
  
  for news_title in soup.find_all("div", class_="list-titles") :
    list_title.append(news_title.get_text())
  
  print(list_title)
  print("-------------------------------------")
  
  for news_summary in soup.find_all("p", class_="list-summary") :
    list_summary.append(news_summary.get_text())
  
  print(list_summary)

if __name__ == "__main__":
  main()