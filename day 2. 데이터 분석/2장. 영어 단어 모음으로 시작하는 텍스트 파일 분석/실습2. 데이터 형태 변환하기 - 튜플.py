# 텍스트 파일을 불러옵니다.
corpus = 'corpus.txt'

def import_as_tuple(filename):
  '''
  (단어, 빈도수)` 튜플로 구성된 리스트를 리턴합니다.
  
  >>> import_as_tumple(corpus)
  [('zoo', '768'), ('zones', '1168'), ... ] 
  '''
  
  tuples = []
  with open(corpus) as file:
    # file에서 line을 읽어올 때 줄바꿈도 같이 읽어오는 문제점이 있다.
    for line in file:
      # 아래 코드를 작성하세요.
      # split하기 전에 strip()을 사용하여 공백 없애기
      split = line.strip().split(',')
      word = split[0]
      freq = split[1]
      new_tuple = (word, freq)
      tuples.append(new_tuple)
  return tuples

# 아래 주석을 해제하고 결과를 확인해보세요.  
print(import_as_tuple(corpus))
