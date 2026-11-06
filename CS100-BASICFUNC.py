''' WRITE A FUNCTION localPhones() that takes string parameter:
text -> s string containing phone numbers seperate by spaces.
Each phone has a format xxx-xxx-xxxx.
The Function returns the list of all phone number with '973' area code.
'''
#ABDULLAH YILDIRIM and PRAKASH JAVADALA GROUP 6
def localPhones(text):
    area='973'
    lst=[]
    newText = text.split()
    for phoneNumber in newText:
        if phoneNumber[0] in area:
            lst.append(phoneNumber)
            
    return lst



t='973-596-300 201-345-2345 973-596-2345 800-345-4321'
print(localPhones(t))#['973-596-300', '973-596-2345']
