import re

def is_palindrome(phrase):
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    if forwards == backwards:
        print('Yes, '+phrase+' is a palindrome.')
    else:
        print("It is not a palindrome.")


print(is_palindrome('anna'))
print(is_palindrome('Anna'))

def my_palindrome(word):
    original = word.lower()
    revWord = original[::-1]
    if original == revWord:
        print('It is palindrome')
    else:
        print('not a palindrome')
    
print(my_palindrome('anna'))