print('this is {} {} {}'.format('a', 'b', 'c'))

print('this is {0} {2} {1}'.format('a', 'b', 'c'))

print('this is {0} {0} {1}'.format('a', 'b', 'c'))

print('this is {A} {B} {C}'.format(A='a', B='b', C='c'))

result = 10/3
print("the result is {r:1.2f}".format(r=result))
# this is how you can precisely control the number of digits after decimal point 

print("the result is {r:10.3f}".format(r=result))
# it'll print 9 whitespaces before the result to make the total width 10 characters

print(f"the result is {result}")
# this is another way to format strings, it's called f-string, 
# it's more concise and easier to read than the format method. It's available in Python 3.6 and above.


name = "purv"

for i , c in enumerate(name):
    print(i, c)
# enumerate is a built-in function that takes an iterable and returns an iterator that produces pairs of index and value. 
# In this case, it will return (0, 'p'), (1, 'u'), (2, 'r'), (3, 'v') for the string "purv".

str = "this is test string."
newstr=""
for i in range(len(str)):
    if i%2 == 0:
        newstr += str[i].upper()
    else:
        newstr += str[i].lower()
print(newstr)

str = input("enter a string: ")

def func(str):
    newstr=""
    for i in range(len(str)):
        if i == 0 or i == 3:
            newstr += str[i].upper()
        else:
            newstr += str[i]

    return newstr

print(func(str))

def func(str):
    words = str.split()
    reversed_words = words[::-1]
    return" ".join(reversed_words)

print(func("this is a test string"))

s = " "
print(s.isspace())

s = {1,2,3}
sc = s.copy()
s.add(4)
print(s)
print(sc)