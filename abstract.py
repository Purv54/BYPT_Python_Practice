# abstract methods are methods that are declared but not implemented in the base class. 
# They must be implemented in the derived class. They are defined using the @abstractmethod decorator from the abc module.

from abc import ABC, abstractmethod

class Animal(ABC): # Inherit from ABC to make the class abstract
    @abstractmethod
    def make_sound(self):
        """Method documentation: Subclasses must implement this method."""
        pass # No implementation

    def move(self):
        """Concrete method with implementation, inherited by subclasses."""
        print("Moving generic way...")

class Dog(Animal):
    def make_sound(self):
        return "Bark!" # Providing the required implementation

mydog = Dog()
print(mydog.make_sound())
# This would raise a TypeError because it doesn't implement make_sound()
# class IncompleteAnimal(Animal):
#     pass
