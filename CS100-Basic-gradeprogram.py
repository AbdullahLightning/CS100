''' WRITE A PROGRAM THAT REPEATEDLY PROMPTS THE USER FOR 10 EXAM SCORES AND ADD THEM TO A LIST.
THEN PRINT THE LIST. THEN, WRITE ADDITIONAL CODE TO CREATE AND PRINT TO THE SCREEN A LIST CONTAINING ALL As
Enter score: 99
Enter score: 9
Enter score: 79
Enter score: 59
Enter score: 99
Enter score: 99
Enter score: 95
Enter score: 99
Enter score: 65
Enter score: 72
List of all scores: [99,9,79,59,99,95,99,65,72]
List of As: [99,99,99,95,99]
'''
#group 6 ABDULLAH YILDIIRM AND PRAKASH JAVADALA
allScores=[]
numofAs=[]
for score in range(10):
    score = int(input('Enter score: '))
    allScores.append(score)
    
for score in allScores:
    if score >= 90:
        numofAs.append(score)
        
print('List of all scores: ', allScores)
print('List of As: ', numofAs)
