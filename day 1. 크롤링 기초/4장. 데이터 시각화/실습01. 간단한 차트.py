# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
import matplotlib.pyplot as plt # 차트 라이브러리
import numpy as np


def main():
  x = np.arange(1, 10)
  y = np.arange(1, 10)

  plt.plot(x, y)
  plt.xlabel('x_chuck')
  plt.ylabel('y_chuck')
  plt.title('sample_chart')

  plt.savefig("image.svg", formate="svg") # 그래프 그림 저장하기
  # elice_utils.send_image("image.svg")

if __name__ == "__main__":
  main()