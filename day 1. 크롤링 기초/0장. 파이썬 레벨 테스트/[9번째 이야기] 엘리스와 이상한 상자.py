class maxMachine :
  def __init__(self) :
    self.numbers = []

  def addNumber(self, n) :
    self.numbers.append(n)
    return self.numbers
      
  def removeNumber(self, n) :
    return self.numbers.remove(n)

  def getMax(self) :
    return max(self.numbers)

  def str(self) :
    return self.numbers
    
def main():

  myMachine = maxMachine()

  myMachine.addNumber(2)
  myMachine.addNumber(5)
  myMachine.addNumber(3)
  myMachine.addNumber(4)
  
  print(myMachine.str())
  print(myMachine.getMax())

  myMachine.removeNumber(5)
  print(myMachine.str())
  
  print(myMachine.getMax())

  myMachine.removeNumber(4)
  print(myMachine.str())

  print(myMachine.getMax())

if __name__ == "__main__":
  main()