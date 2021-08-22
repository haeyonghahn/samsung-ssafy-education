# from elice_utils import EliceUtils

# elice_utils = EliceUtils()

def main():
  text_one = "나는 짜장면을 좋아합니다."
  
  text_list = text_one.split()

  print(text_list)
  
  print(text_list[0])
  print(text_list[1])
  print(text_list[2])
  
  text_result = text_list[0] + text_list[1] + text_list[2]
  print(text_result)
  
  text_result = text_list[0] + " " + text_list[1] + " " + text_list[2]
  print(text_result)
  
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  
  text_two = "나는!트와이스를!좋아합니다"
  print(text_two.split("!"))
  
  sentence_1 = "나는 트와이스를 좋아합니다."
  sentence_2 = "나는 방탄소년을 좋아합니다."
  sentence_3 = "나는 걸스데이를 좋아합니다."
  
  #헷갈릴 때
  #print(sentence_1[0])
  #print(sentence_1[2])
  #print(sentence_1[0:4])
  
  print(sentence_1[3:7])
  print(sentence_2[3:7])
  print(sentence_3[3:7])
  
  print("-------------------------------------------------------")
  
  st1 = "나는 수학을 좋아합니다."
  st2 = "나는 과학을 좋아합니다."
  
  print(st1)
  print(st2)
  
  print(st1.replace("수학", "도덕"))
  print(st2.replace("과학", "도덕"))
    
if __name__ == "__main__":
  main()