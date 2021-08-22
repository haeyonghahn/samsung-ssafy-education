# CSV 모듈을 임포트합니다.
import csv

def get_titles_of_long_books(books_csv):
  '''
  페이지 수가 250이 넘는 책들의 제목을 리스트로 리턴합니다.
  '''
  
  with open(books_csv, 'rt', encoding='UTF8') as books:
    reader = csv.reader(books, delimiter=',')
    # 함수를 완성하세요.
    # csv를 가져올 때, 문자열 형식으로 데이터를 가져오기 때문에
    # int를 씌워 정수 형태로 변환해야됨
    is_long = lambda row: int(row[3]) > 250
    get_title = lambda row: row[0]
    
    long_books = filter(is_long, reader)
    long_book_titles = map(get_title, long_books)
    
    # filter도 list로 리턴하는 이유는
    # with로 사용하면 파일이 닫혀서 나중에 파일을 가져오는데
    # 오류가 발생하므로 list로 전환하여 연산을 수행하기 위한 것임
    return list(long_book_titles)


# 작성한 함수를 테스트합니다. 주석을 해제하고 실행하세요.
books  = 'books.csv'
titles = get_titles_of_long_books(books)
for title in titles:
  print(title)

