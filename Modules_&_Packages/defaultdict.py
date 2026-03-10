from collections import defaultdict

d = defaultdict(lambda: 'Not Present')

d['age'] = 21
d['gender'] = "Male"
d["income"]

print(d)
# defaultdict is a subclass of the built-in dict class.
# It overrides one method and adds one writable instance variable. 
# The remaining functionality is the same as for the dict class. 
# The first argument of the defaultdict constructor is called default_factory. 
# It is used to provide default values for the dictionary. 
# If you try to access or modify a key that does not exist in the dictionary,
# it will return the value provided by default_factory instead of raising a KeyError.