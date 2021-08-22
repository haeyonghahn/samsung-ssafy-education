class Rectangle :

  def __init__(self, width, height) :
    self.width = width
    self.height = height

  def area(self) :
    return self.width * self.height

class Square(Rectangle) :
    
  def __init__(self, side) :
    self.side = side
      
  def area(self) :
    return self.side * self.side

def main() :
  alice = Rectangle(10, 20)
  print(alice.area())

  bob = Square(10)
  print(bob.area())

if __name__== "__main__":
  main()