#Write a program that creates a list of 5 exam scores from scratch.
#Start with an empty list and prompt the user for each exam score(integers)
#The program prints to the screen the list of those 5 scores and the number of perfect scores in it, i.e. 100s
#ABDULLAH YILDIRIM AND PRAKASH JAVADALA
myList = []

exam1=input('what is exam score 1 : ')
exam1= int(exam1)

myList.insert(len(myList),exam1)

exam2=input('what is exam score 2 : ')
exam2=int(exam2)

myList.insert(len(myList),exam2)

exam3=input('what is exam score 3 : ')
exam3=int(exam3)

myList.insert(len(myList),exam3)

exam4=input('what is exam score 4 : ')

exam4=int(exam4)
myList.insert(len(myList),exam4)

exam5=input('what is exam score 5 : ')

exam5=int(exam5)
myList.insert(len(myList),exam5)

print(myList)

print(myList.count(100))
