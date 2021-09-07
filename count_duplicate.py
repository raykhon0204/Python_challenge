list1 = ['a', 'b', 'c', 'b', 'c', 'e', 'm', 'e', 'm']

sorted_list = sorted(list1)
duplicates = []
for i in list1:
    if sorted_list.count(i)>1:
        if i not in duplicates:
            duplicates.append(i)

print('Number of duplicates ', len(duplicates))

print('\Duplicate items are ', duplicates)