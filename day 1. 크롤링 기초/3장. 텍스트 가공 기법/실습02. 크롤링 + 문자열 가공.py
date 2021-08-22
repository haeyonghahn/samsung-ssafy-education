# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
import urllib.request
from bs4 import BeautifulSoup

def main():
  url = "http://www.newsis.com/eco/list/?cid=10400&scid=10404"
  req = urllib.request.Request(url)
  sourcecode = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(sourcecode, "html.parser")
  
  for text in soup.find_all("strong", class_="title"):

    #print(text.get_text())
    # -1로 표시되는 것은 ...을 찾을 수 없는 것
    #print(text.get_text().find("..."))
    
    num = text.get_text().find(",")
    #print(text.get_text()[0:num])
    #print(num)
    if (num != -1):
      print(text.get_text()[0:num])
    else:
      print(text.get_text())
        
    # 예외처리한 이유는 num이 -1일 경우 슬라이싱 때문에
    # 뒤의 문자가 잘리기 때문

if __name__ == "__main__":
  main()