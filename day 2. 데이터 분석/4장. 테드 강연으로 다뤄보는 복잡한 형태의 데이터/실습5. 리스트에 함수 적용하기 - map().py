# CSV 모듈을 임포트합니다.
import csv

def get_titles(books_csv):
  '''
  CSV 파일을 읽고 제목의 리스트를 리턴합니다. 
  '''
  '''
  여기서 주의할 점은 with으로 file을 접근하면
  return한 후 바로 파일을 닫게되어 나중에 파일에 접근하는 map같은 경우
  오류가 발생할 수 있다. 그래서 return할 때 list(titles)로 묶어서
  map 연산을 수행하고 끝내면 된다.
  '''
  with open(books_csv, 'rt', encoding='UTF8') as books:
    reader = csv.reader(books, delimiter=',')
    # 함수를 완성하세요.
    get_title = lambda row: row[0]
    titles = map(get_title, reader)
    #titles = []
    #for row in reader :
        #titles.append(row[0])
    return list(titles)


# 작성한 코드를 테스트합니다. 주석을 해제하고 실행하세요.
books = 'books.csv'
titles = get_titles(books)
for title in titles:
    print(title)