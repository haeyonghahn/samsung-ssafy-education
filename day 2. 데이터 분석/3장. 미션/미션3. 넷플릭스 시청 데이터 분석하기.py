import matplotlib.pyplot as plt
import json
from operator import itemgetter

# from elice_utils import EliceUtils
from movies import titles


# 데이터 가공하는 함수
def preprocess_data(filename):
  '''
  입력 받은 JSON 형식의 데이터를 딕셔너리로 변환하여 리턴합니다. 이때 int()를 이용해 key를 정수로 설정합니다.
  
  >>> preprocess_data('netflix.json')
  {30: [2621442, 1048579, ...], ..., 17627: [2621442, 1048579, ...]}
  {
      1번 작품 : [사용자1, 사용자2, 사용자3],
      2번 작품 : [사용자3, 사용자5, 사용자6],
  }
  
  {
      "30" : [192, 293, 486],
      "712" : [678, 561, 567],
  }
  '''
  
  processed = {}
  with open(filename) as file:
    # 입력 받은 JSON 파일을 불러와 loaded에 저장합니다.
    loaded = json.loads(file.read())
    # JSON 형식의 데이터에서 영화와 사용자 정보를 하나씩 가져옵니다.
    for title, users in loaded.items() :
      title = int(title)
      # processed 딕셔너리에 title을 키로, user를 값으로 저장합니다.
      processed[title] = users       
  return processed

# 데이터 가공하는 함수
def reformat_data(title_to_users):
  '''
  (작품 별 시청한 사용자) 딕셔너리를 (사용자 별 시청 작품) 딕셔너리로 변환합니다.
  
  >>> reformat_data(title_to_users('netflix.json'))
  {2621442: [30, 17627, ...], ...}
  예를 들어,
  {
      1번 작품 : [사용자1, 사용자2, 사용자3]
      2번 작품 : [사용자4, 사용자2, 사용자 5]
  }
  이것을
  {
      사용자1 : [1번 작품, 2번 작품]
      사용자4 : [2번 작품, 5번 작품]
  }
  이런 식으로 변경해 준다는 것
  '''
  
  user_to_titles = {}
  # 입력받은 딕셔너리에서 영화와 사용자 정보를 하나씩 가져옵니다.
  for title, users in title_to_users.items() :
    # user_to_titles에 사용자 정보가 있을 경우 사용자의 영화 정보를 추가합니다. 이때 영화 정보는 리스트형으로 저장됩니다. 
    for user in users : # users = [사용자1, 사용자2, 사용자3]
      if user in user_to_titles :
        user_to_titles[user].append(title)
      # 만약에 사용자 정보가 없다면(사용자가 처음 나온 경우)
      # users_to_titles[사용자1] = 1번 작품
      else :
        user_to_titles[user] = [title]
  return user_to_titles


def get_closeness(title_to_users, title1, title2):
  '''
  두 작품의 유사도를 구합니다. 이때 유사도는 (두 작품을 모두 본 사용자) / (두 작품 중 하나라도 본 사용자)와 같습니다.
  
  >>> get_closeness(preprocess_data('netflix.json'), 14312, 14454)
  0.66331
  '''
  
  # title_to_users를 이용해 title1를 시청한 사용자의 집합을 저장합니다.
  title1_users = set(title_to_users[title1]) # 1번 작품을 본 사용자들의 리스트임.
  # title_to_users를 이용해 title2를 시청한 사용자의 집합을 저장합니다.
  title2_users = set(title_to_users[title2]) # 2번 작품을 본 사용자들의 리스트임
  
  # 두 작품을 모두 본 사용자를 구합니다.
  both = len(title1_users & title2_users)
  # 두 작품 중 하나라도 본 사용자를 구합니다.
  either = len(title1_users | title2_users)

  return both / either

# 선호도 예측
def predict_preference(title_to_users, user_to_titles, user, title):
  '''
  작품1과 사용자A가 주어졌을 때, 예상 선호도를 계산합니다.
  작품1에 대한 사용자A의 예상 선호도는 사용자A가 시청한 모든 작품과 작품1 유사도의 평균값입니다. 
  예로, 사용자A가 시청한 3개의 작품과 작품1의 유사도가 0.6, 0.4, 0.5일 때, 선호도 점수는 0.5입니다.
  '''
  
  # user_to_titles를 이용해 user가 시청한 영화를 저장합니다.
  watched = user_to_titles[user]
  # get_closeness() 함수를 이용해 유사도를 계산합니다.
  closeness_list = []
  for watched_title in watched :
    # watched_title과 title 순서 바껴도 상관없음
    closeness = get_closeness(title_to_users, watched_title, title)
    closeness_list.append(closeness)
  
  closeness_sum = 0
  for closeness in closeness_list :
    closeness_sum += closeness
  return closeness_sum / len(closeness_list)

def main():
  filename = 'netflix.json'
  title_to_users = preprocess_data(filename)
  user_to_titles = reformat_data(title_to_users)
  
  lotr1 = 2452                # 반지의 제왕 - 반지 원정대
  lotr2 = 11521               # 반지의 제왕 - 두 개의 탑
  lotr3 = 14240               # 반지의 제왕 - 왕의 귀환
  
  killbill1 = 14454           # 킬 빌 - 1부
  killbill2 = 457             # 킬 빌 - 2부
  
  jurassic_park = 14312       # 쥬라기 공원
  shawshank = 14550           # 쇼생크 탈출
  
  print("[유사도 측정]")
  title1 = lotr1
  title2 = lotr2
  description = "{}와 {}의 작품 성향 유사도".format(titles[title1], titles[title2]) #titles는 movies 모듈의 변수
  # 0.9 이런 것보다는 직관적으로 보기 위해 90%로 나오기 위해 100을 곱하고 반올림함
  closeness = round(get_closeness(title_to_users, title1, title2) * 100)
  print("{}: {}%".format(description, closeness))
  
  print("-------------------------------------------------------")
  
  username = 'elice'
  new_utt = user_to_titles.copy()
  new_utt[username] = [lotr1, lotr2, lotr3]
  
  print("[{} 사용자를 위한 작품 추천]".format(username))
  preferences = []
  preferences = [(title, predict_preference(title_to_users, new_utt, 'elice', title)) for title in title_to_users.keys()]
  print(preferences[:5])
  preferences.sort(key=itemgetter(1), reverse=True)
  # for p in preferences[:6]:
  #   print("{} ({}%)".format(titles[p[0]], round(p[1] * 100)))
        
if __name__ == "__main__":
  main()