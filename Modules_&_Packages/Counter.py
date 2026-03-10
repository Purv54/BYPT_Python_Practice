from collections import Counter

list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
counter = Counter(list)
print(counter)

counter = Counter('hello world')
print(counter)

str = "Hello this is a counter to test which word repeates how many times in this string"
words = str.split()
counter = Counter(words)
print(counter)

letters = "aaabbbdddjiwiieuuu"
counter = Counter(letters)
print(counter.most_common(3))
# most_common() method returns a list of the n most common elements and their counts from the most common to the least. 
# If n is not specified, it returns all elements in the counter.
print(list(counter))