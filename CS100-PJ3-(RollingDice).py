'''Define a function playGame() that 'rolls' two dice repeatedly until
they both land on a 6. The function returns the number of times they were both
odds.
for example below is a sequence of two dice being rolled:
2 4
1 5
2 5
5 3
4 5
6 2
1 6
6 6
the function in this case would return.'''
#GROUP 6 ABDULLAH YILDIRIM AND PRAKASH JAVADALA
import random

def playGame():
    oddCount=0
    Dice1=0
    Dice2=0
    while (Dice1 != 6 or Dice2 != 6):
        Dice1 = random.randint(1, 6)
        Dice2 = random.randint(1, 6)
        print(Dice1, Dice2)
        if Dice1 == 6 and Dice2 == 6:
            print(run)
            break
        if Dice1 % 2 == 1 and Dice2 % 2 == 1:
            oddCount += 1
            
        
    return oddCount
    

print('Number of rolls for both dice being odd: ',playGame())    
