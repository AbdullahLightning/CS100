#CS100 RK956 ABDULLAH YILDIRIM HW8 WHILE LOOP
def twoWords(length,firstLetter):

    fWord = "" 
    sWord= ""

    while True:

        fWord = input('A ' + str(length) + '-letter word please: ')
        if length == len(fWord):
            break
    while True:
        sWord = input('A word beginning with ' + firstLetter+ ' please')
        if sWord[0] == firstLetter.upper() or sWord[0] == firstLetter.lower():
            break
    return [fWord,sWord]

print(twoWords(4,'B'))

#q2
def twoWordsV2(length, fLetter):
    word1 = ""
    word2= ""
    while(len(word1)!=length):
        word1 = input('A ' + str(length) + '-letter word please: ')
    while(word2!=fLetter): 
      word2 = input('A word beginning with ' + (fLetter)+ ' please: ')
      if word2[0] == fLetter.upper() or word2[0] == fLetter.lower():
          return [word1,word2]
print(twoWordsV2(4,'B'))

#q3
def enterNewPass():
    while True:
        respond = input("Please enter password 8-15 characters including 1 digit: ")
        hasDigit = False
        
        for i in respond:  
            if i.isdigit():
                hasDigit = True
                break

        if not hasDigit or (len(respond) < 8 or len(respond) > 15):
            if len(respond) < 8 or len(respond) > 15:
                print("The password's characters must be 8-15!")
            if not hasDigit:
                print("Password must include one digit!")
        else:
            print("Password is valid:", respond)
            break  

enterNewPass()
#Q4
import random

def GuessNumb():
    print("I'm thinking of a number between 0-50. You have 5 tries to guess it.")

    guess = random.randint(0, 50)  
    attempts = 0  

    while attempts < 5:  
        userin = int(input(f"Guess #{attempts + 1}: "))  
        attempts += 1  

        if userin == guess:  
            print(f"Wow, you got it mate! The number was {guess}.")
            return  
        elif userin > guess:  
            print("Your guess is too high.")
        else:  
            print("Your guess is too low.")

    print(f"Sorry, you've used all your tries. The number was {guess}.")

GuessNumb()



