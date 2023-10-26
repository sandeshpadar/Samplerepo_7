# how to addition,  multiplication, substraction and division in two number using class

class function:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def Addition(self):
        print('Addition of', self.num1, 'and', self.num2, 'is', self.num1+self.num2)

    def Multiplication(self):
        print('Addition of', self.num1, 'and', self.num2, 'is', self.num1*self.num2)

    def Substraction(self):
        print('Addition of', self.num1, 'and', self.num2, 'is', self.num1-self.num2)

    def Division(self):
        print('Addition of', self.num1, 'and', self.num2, 'is', self.num1/self.num2)

obj_function = function(50, 100)
obj_function.Addition()
obj_function.Multiplication()
obj_function.Substraction()
obj_function.Division()
