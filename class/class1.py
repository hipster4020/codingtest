class Calculator:
    # 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second
        print(f"init first : {self.first}")
        print(f"init second : {self.second}")
    
    # sum method
    def add(self):
        sum = self.first + self.second
        return sum