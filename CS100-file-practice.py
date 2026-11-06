#write a python program thatbopens the CS100FILEGRADES.txt file
#and prints every student record one at a time.

inFile = open('CS100FILEGRADES.txt', 'r')

#Approach -> use a for-loop
'''for line in inFile:
   # print(line)
    tokens = line.split()
    if int(tokens[1]) >= 90:
        print(tokens[0])'''
#approach 2 -> use file function readlines()
'''myList = inFile.readlines()'''
#use this list to print to the screen the names of the students who get an A
'''for eachLine in myList:
    tokens = eachLine.split()
    if int(tokens[1]) >= 90:
        print(tokens[0])'''
        
        
#print(myList)

#approach 3-> use file function read()
'''content = inFile.read().strip('\n')
#print(content)
#split the content by \n
lineList = content.split('\n')
for line in lineList:
    #'jake 85' -> split this line
    tokens = line.split()
    if int(tokens[1]) >= 90:
        print(tokens[0])'''

#print(len(inFile.read().strip('\n').split()))

#approach 4 -> use file function readline()
'''line = inFile.readline()
print(line)

line = inFile.readline()
print(line)
'''
# genelde ilk 3 approach daha onemli cok cok kullaniriz.
#use content and write some magic code to print to the screen the names of
#students who get an A
#Use any of these reading approaches to read and then write to a aScores.txt
#file the names of the students who get an A
outfile = open('aScores.txt', 'w')
for line in inFile:
    tokens = line.split()
    if int(tokens[1]) >= 90:
        #write the name of students to the file
        outfile.write(tokens[0]+'\n')
        print(tokens[0])
inFile.close()
outfile.close()
