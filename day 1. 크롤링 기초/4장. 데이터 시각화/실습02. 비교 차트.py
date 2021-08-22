# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
from matplotlib import pyplot as plt

def main():
  print("비교 차트 그리기")

  plt.xlabel("person")
  plt.ylabel("grade")

  # Python
  plt.plot(["a", "b", "c", "d", "e"], [100, 97, 46, 28, 84])

  # Java
  plt.plot(["a", "b", "c", "d", "e"], [58, 28, 37, 83, 22])

  plt.savefig("image.svg", format="svg")
  # elice_utils.send_image("image.svg")

if __name__ == "__main__":
  main()