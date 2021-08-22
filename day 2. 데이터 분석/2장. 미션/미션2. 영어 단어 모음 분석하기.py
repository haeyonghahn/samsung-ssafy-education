# 프로젝트에 필요한 패키지를 import합니다.
# 어떤 데이터의 모음이 주어졌을 때 그 데이터 중에서 특정한 원소를 가져오는 함수
from operator import itemgetter 
from collections import Counter
from string import punctuation
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# from elice_utils import EliceUtils
# elice_utils = EliceUtils()

# corpus.txt 파일을 우리가 원하는 데이터 구조로 변환하는 메소드
def import_corpus(filename):
  '''
  단어와 빈도수 데이터가 담긴 파일 한 개를 읽고 (단어, 빈도수) 꼴의 튜플로 구성된 리스트를 리턴합니다.
  
  >>> import_corpus('corpus.txt')
  [('zoo', 768), ('zones', 1168), ..., ('a', 2150885)]
  '''
  # 튜플을 저장할 리스트를 생성합니다.
  corpus = []
  
  # 매개변수로 입력 받은 파일을 열고 읽습니다.
  with open(filename) as file :
    for line in file :
      # split으로 분류를 하면
      # split = ['zoo', '768'] 이런 식으로 빈도수가 문자열로 들어가기 때문에
      # 나중에 int로 변환해주는 작업이 필요하다.
      split = line.strip().split(',')
      word = split[0]
      freq = int(split[1])
      word_data = (word, freq)
      corpus.append(word_data)
    # 텍스트 파일의 각 줄을 (단어, 빈도수) 꼴로 corpus에 저장합니다.
  return corpus

def create_corpus(filenames):
  '''
  텍스트 파일 여러 개를 한 번에 읽고 (단어, 빈도수) 꼴의 튜플로 구성된 리스트를 리턴합니다.
  
  >>> create_corpus(['chapter1.txt', 
                      'chapter2.txt',
                      'chapter3.txt'])
  [('Down', 3), ('the', 175), ..., ('party', 1)]
  '''
  # 단어를 저장할 리스트를 생성합니다.
  words = []
  
  # 여러 파일에 등장하는 모든 단어를 모두 words에 저장합니다.
  for filename in filenames :
    with open(filename) as file :
      # 우리가 여기서 line in file을 사용하지 않는 이유는
      # 데이터를 가공할 필요가 없고 한번에 모든 것을 읽어와야하기 때문이다.
      # 그래서 읽어온 소설을 content에 저장
      content = file.read().strip()
      # 이 때 문장부호를 포함한 모든 특수기호를 제거합니다. 4번째 줄에서 임포트한 punctuation을  이용하세요.
      for symbol in punctuation:
        content = content.replace(symbol, '')
      for word in content.split() :
        words.append(word)

  # words 리스트의 데이터를 corpus 형태로 변환합니다. Counter() 사용 방법을 검색해보세요.
  # 이 두 줄의 코드는 다음 시간에 아주 자세하게 배울 것이다.
  #from stopwords import stopwords
  corpus = Counter(words)
  #for stopword in stopwords :
      #corpus[stopword] = 0 # corpus = {"!":100, "?":50,} {1 : 1, 5 : 4}
  #print(corpus.items())
  return list(corpus.items())

def filter_by_prefix(corpus, prefix):
  '''
  corpus의 데이터 중 prefix로 시작하는 단어 데이터만 추립니다. 한 줄 코드를 이용해 작성해보세요.
  
  >>> filter_by_prefix(import_corpus('corpus.txt'), 'ze'))
  [('zero', 2286), ('zealand', 2636)]
  '''
  filtered = []
  #new_tuple = (1, 3)
  #a, b = new_tuple
  #a = 1, b = 3
  # 1번 스타일
  for word, freq in corpus :
      if word.startswith(prefix) :
          filtered.append((word, freq))
                  
  # 2번 스타일
  '''
  for word_data in corpus :
    if word_data[0].startswith(prefix) :
      filtered.append(word_data)
  '''
  return filtered

# itemgetter(0)([1,2,3]) 과 같은 것
def get_freq(word_data) :
  #print(word_data)
  return word_data[1]

def most_frequent_words(corpus, number):
  '''
  corpus의 데이터 중 가장 빈도가 높은 number개의 데이터만 추립니다. 한 줄 코드를 이용해 작성해보세요.
  
  most_frequent_words(import_corpus('corpus.txt'), 2))
  >>> [('the', 6187927), ('of', 2941790)]
  '''
  # 빈도수가 낮은 것부터 출력되므로 reverse시킴
  #print(corpus[0])
  sorted_corpus = sorted(corpus, key=get_freq, reverse=True) 
  
  return sorted_corpus[:number]

def draw_frequency_graph(corpus):
  # 막대 그래프의 막대 위치를 결정하는 pos를 선언합니다.
  pos = range(len(corpus))
  
  # 튜플의 리스트인 corpus를 단어의 리스트 words와 빈도의 리스트 freqs로 분리합니다.
  words = [tup[0] for tup in corpus]
  freqs = [tup[1] for tup in corpus]
  
  # 한국어를 보기 좋게 표시할 수 있도록 폰트를 설정합니다.
  # 다음 시간에 배울 함수
  font = fm.FontProperties(fname='./NanumBarunGothic.ttf')
  
  # 막대의 높이가 빈도의 값이 되도록 설정합니다.
  plt.bar(pos, freqs, align='center')
  
  # 각 막대에 해당되는 단어를 입력합니다.
  # rotation="vertical"로 변경해볼 것
  plt.xticks(pos, words, rotation='horizontal', fontproperties=font)
  
  # 그래프의 제목을 설정합니다.
  plt.title('단어 별 사용 빈도', fontproperties=font)
  
  # Y축에 설명을 추가합니다.
  plt.ylabel('빈도', fontproperties=font)
  
  # 단어가 잘리지 않도록 여백을 조정합니다.
  plt.tight_layout()
  
  # 그래프를 표시합니다.
  plt.savefig('graph.png')
  # elice_utils.send_image('graph.png')

def main(prefix=''):
  # import_corpus() 함수를 통해 튜플의 리스트를 생성합니다.
  corpus = import_corpus('corpus.txt')
  
  # head로 시작하는 단어들만 골라 냅니다.
  # 만약에 prefix=''이면 모든 단어들을 추출해낸다. 모든 단어들을 볼 수 있다.
  prefix_words = filter_by_prefix(corpus, prefix)
  
  # 주어진 prefix로 시작하는 단어들을 빈도가 높은 순으로 정렬한 뒤 앞의 10개만 추립니다.
  top_ten = most_frequent_words(prefix_words, 10)
  
  # 단어 별 빈도수를 그래프로 나타냅니다.
  draw_frequency_graph(top_ten)
  
  print("----------------------------------------------------------")
  
  # 'Alice in Wonderland' 책의 단어를 corpus로 바꿉니다.
  alice_files = ['alice/chapter{}.txt'.format(chapter) for chapter in range(1, 6)]
  alice_corpus = create_corpus(alice_files)
  
  top_ten_alice = most_frequent_words(alice_corpus, 10)
  draw_frequency_graph(top_ten_alice)

if __name__ == '__main__':
  main()
