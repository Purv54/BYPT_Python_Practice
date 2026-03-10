import re

phrase = "this is 3 a regular 4 expression example"
cleared = re.findall(r'[^\d]+', phrase)

print(''.join(cleared))
# The re module provides support for regular expressions in Python.
# The re.findall() function returns a list of all non-overlapping matches of the pattern in the string. 
# The pattern r'[^\d]+' matches one or more characters that are not digits. 
# The ^ character inside the square brackets negates the character class, so it matches any character that is not a digit. 
# The + character means that the preceding character class must occur one or more times. 
# The result is a list of all the substrings in the original string that do not contain digits. 

phase2 = "this is . a regular ?expression example!"
cleared2 = re.findall(r'[^.?!]+', phase2)
print(cleared2)
print(''.join(cleared2))