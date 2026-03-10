from collections import namedtuple

Dog = namedtuple('Dog', ['name', 'age', 'breed'])
my_dog = Dog(name='Buddy', age=5, breed='Golden Retriever')
print(my_dog)
print(type(my_dog))
print(my_dog.name)
print(my_dog.age)
print(my_dog.breed)

# namedtuple is a factory function for creating tuple subclasses with named fields. 
# It returns a new tuple subclass named typename. 
# The first argument is the name of the class to be created, and the second argument is a list of field names. 
# The resulting class has an __init__() method that takes the field names as arguments and assigns them to instance variables. 
# It also has a __repr__() method that returns a string representation of the object, and a __getitem__() method that allows you to access the fields by name or by index.
# namedtuple is useful for creating simple classes that are primarily used to store data and do not require additional methods or behavior.
    