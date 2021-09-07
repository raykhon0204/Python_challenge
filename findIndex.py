#find the index of a given number
list1 = [5,2,6,8,4,9,10,7,6]

def findIndex(numbers, num):
    for i, j in enumerate(numbers):
        if j == num:
            print('the index of '+str(num)+ ' is ' +str(i))
        else:
            print('The number you provided is not found')

print(findIndex(list1, 9))