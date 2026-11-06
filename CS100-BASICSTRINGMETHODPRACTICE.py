'''WRITE A FUNCTION analyzeText() that takes a paramater:
text -> a string containing words and white spaces
The function return the number of words in text that end ina vowel.
'''
def analyzeText(text):
    newText = text.lower()
    wordsList = newText.split()
    vowels = 'aeiou'
    count=0
    for word in wordsList:
        if word[-1] in vowels:
            count +=1
    return count       

myText = 'an APPLE a day keeps the doctor away'
print(analyzeText(myText)) #3
