# list = [2,4,1,10,11,100,189,3,5,6]
# newlist=list.sort()
# print(newlist)

# # the sort method sorts the list in place and returns None, so newlist is None

# list.sort()
# print(list)

# list2 = [1,2,[3,4]]
# print(list2[2][1])

list1 = [1,2,3]
list2 = ['a', 'b', 'c']

for items in zip(list1, list2):
    print(items)
print(list(zip(list1, list2)))
# zip is a built-in function that takes two or more iterables and returns an iterator 
# that produces tuples of corresponding elements from the iterables. In this case, 
# it will return (1, 'a'), (2, 'b'), (3, 'c')

# from random import shuffle

list3 = [1,2,3,4,5]
# help(list3.clear)

# shuffle(list3)
# print(list3)
# shuffle(list3)
# print(list3)
# shuffle(list3)
# print(list3)

# we can't write newlist = shuffle(list3) because shuffle returns None, it shuffles the list in place.
# shuffle is a built-in function that takes a list and shuffles it in place.