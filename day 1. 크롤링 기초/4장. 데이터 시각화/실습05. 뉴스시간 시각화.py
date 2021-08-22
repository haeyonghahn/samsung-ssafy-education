# from elice_utils import EliceUtils

# elice_utils = EliceUtils()

import urllib.request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# 뉴스 사이트 기사 크롤링 -> 데이터를 가공 -> 시각화까지
def main():
	
  url = "http://news.jtbc.joins.com/section/index.aspx?scode=20"
  sourcecode = urllib.request.urlopen(url).read()
  soup = BeautifulSoup(sourcecode, "html.parser")


  time_list = []

  #for i in soup.find_all("span", class_="date") :
    #   print(i.get_text())
  
  for i in range(3,22):
    time_list.append(soup.find_all("span", class_="date")[i].get_text().strip())
  print(time_list)
  
  print("------------------------------------------------")
  time_edit = []

  for i in range(0, len(time_list)) :
    time_edit.append(time_list[i][8:10])

  first_count = 0
  second_count = 0

  for i in range(0, len(time_edit)) :
    if (time_edit[i] == "28") :
      first_count = first_count + 1
    else :
      second_count = second_count + 1

  print(first_count)
  print(second_count)

  slices_hours = [first_count, second_count]
  activities = ['first_day', 'second_day']
  colors = [ 'gray', 'blue']
  plt.pie(slices_hours, labels=activities, colors=colors, startangle=90, autopct='%.1f%%')
  
  plt.savefig("image.svg", format="svg")
  # elice_utils.send_image("image.svg")

if __name__ == "__main__":
  main()