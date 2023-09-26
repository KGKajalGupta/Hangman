import random

print("         Welcome in Number Guessing Game")
print("\nRules")
print("There is a random number guess by computer \nYou have to guess that number \nYou can guess that number untill hangman died\n")

'''
   |
   0
 / | \
  / \
  
I have to add this in this
'''
class Number_Guessing:
    count = 1

    hangman = ["    |\n\n\n","    |\n    0\n\n","    |\n    0\n /\n\n","    |\n    0\n / |\n\n","    |\n    0\n / | \\\n\n","    |\n    0\n / | \\ \n  /\n","    |\n    0\n / | \\ \n  / \\\n"]
    
    def __init__(self, number):
        self.number = number
        self.user_guess()

    def user_guess(self):
        if self.count>7:
            print(f"\nSorry! Out of Move\U0001F622 \nWell played \U0001F600 \nThat Number was {self.number}\n")
            self.restart()
        user_input = int(input("guess a number : "))
        self.check_number(user_input)

    def restart(self):
        ask = input("Do you want to play again: ")
        if ask in ("y", "Y", "YES", "yes", "Yes", "YEs", "YeS", "yES", "yEs", "ySe"):
            Input()
        else:
            print("\nThank You!  \nHave a nive day \U0001F600 \n")
            quit()
    def check_number(self, num):
        if num==self.number:
            print("\nCongratulations! Your guess is correct", "\U0001F929 \n")
            self.restart()
        elif num>self.number:
            if num-self.number<=5:
                print("You are too close, Think little small number\n")
            elif num-self.number<=25:
                print("You are close, Think small number\n" )
            else:
                print("You are very far from number\n")
        elif num<self.number:
            if self.number - num <= 5:
                print("You are too close, Think little large number\n")
            elif self.number - num <= 25:
                print("You are close to number, Think large number\n")
            else:
                print("This is too close, Think little large number\n")

        # print(f"There is {5-self.count} chance left\n")
        print(self.hangman[self.count-1])
        self.count += 1
        self.user_guess()


class Input:
    def __init__(self):
        num = random.randint(10, 150)
        Number_Guessing(num)

Input()