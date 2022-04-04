'''
Lab 11 QN.1 
Done By: 1802965
'''
class Calculator:
    def __init__(self):
        self.output = 0
    
    def adder(self, input1, input2):
        self.output = input1 + input2
        self.displayOutput()
    
    def subtractor(self, input1, input2):
        self.output = input1 - input2
        self.displayOutput()
    
    def multiply(self, input1, input2):
        self.output = input1 * input2
        self.displayOutput()
    
    def divide(self, input1, input2):
        self.output = input1 / input2
        self.displayOutput()

    def displayOutput(self):
        print(self.output)
    
    def clear(self):
        self.output = 0


def main():
    myCalc = Calculator()
    print("Addition: ")
    myCalc.adder(5,1)
    print("\nSubtraction: ")
    myCalc.subtractor(7,3)
    print("\nMultiplication: ")
    myCalc.multiply(8,2)
    print("\nDivision: ")
    myCalc.divide(10,2)
    myCalc.clear()
    myCalc.displayOutput()


if __name__ == "__main__":
    main()