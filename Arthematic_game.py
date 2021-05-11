import time
import random

class Arthematic_Game:
    def __init__(self,No_Questions):
        self.No_Questions = No_Questions
    def Generate_Questions(self):
        value_1 = random.randint(1,25)
        value_2 = random.randint(1,25)
        operator = random.choice(['+','-','*','//'])
        if operator == '+':
            answer = value_1+value_2
        elif operator == '-':
            answer = value_1-value_2
        elif operator == '*':
            answer = value_1 * value_2
        elif operator == '//':
            answer = value_1//value_2
        else:
            print("Please check again !!!!")
        question = str(value_1)+"  "+operator+"  "+str(value_2)+" "+" : "
        return question,answer
    def Play_Game(self):
        correct = 0
        in_correct = 0
        for i in range(1,self.No_Questions+1):
            print("The Question No is :",i)
            question,answer = self.Generate_Questions()
            print(question)
            Answer = int(input("Enter your answer : "))
            if Answer == answer :
                correct+=1
            else:
                in_correct+=1
            print()
        Final_result  = (correct /self.No_Questions)*100
        Result = round(Final_result,2)
        print("Your pass percentage is "+str(Result)+"%")
Arthe = Arthematic_Game(10)
Arthe.Play_Game()
