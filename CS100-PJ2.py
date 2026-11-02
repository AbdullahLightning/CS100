# Python Function Practice
# Exercises using parameters, return values,
# string manipulation, loops, and conditionals.
def display_invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount} is due: {due_date}')

display_invoice('yldrm',200,'09/30')


def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first +' ' + last
full_name = create_name('abdullah', 'yldrm')
print(full_name)

def odd_num(lst):
    count=0
    for num in lst:
        if num % 2 != 0:
            count+=1
    return count        
numbers=[0,1,2,3,4,5,6,7]
print(odd_num(numbers))

