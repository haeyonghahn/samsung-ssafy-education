# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
import openpyxl
from matplotlib import pyplot as plt

def main():
  # 엑셀파일 열기
  wb = openpyxl.load_workbook('data.xlsm')

  # 현재 Active Sheet 얻기
  ws = wb.active

  year = []
  grade1 = []
  grade2 = []
  grade3 = []

  # 점수 읽기 column
  for c in ws.columns :
    year.append(c[0].value)
    grade1.append(c[1].value)
    grade2.append(c[2].value)
    grade3.append(c[3].value)

  plt.xlabel('year')
  plt.ylabel('grade')

  plt.plot(year, grade1)
  plt.plot(year, grade2)
  plt.plot(year, grade3)

  plt.savefig("image.svg", format="svg")
  # elice_utils.send_image("image.svg")

if __name__ == "__main__":
  main()