from class1 import Calculator

def main():
    # 상속
    class MoreCal(Calculator):
        def pow(self):
            pow = self.first ** self.second
            return pow
    
    # a = MoreCal(2, 3)
    # print(a.pow())
    
    
    # overriding
    class ChangeCal(Calculator):
        def add(self):
            sum = self.first + self.first
            return sum
        
    a = ChangeCal(4, 2)
    print(a.add())
    b = Calculator(4, 2)
    print(b.add())
    
    
    
if __name__ == "__main__":
    main()