def cool():
    
    def supercool():
        return "super cool"
    
    return supercool

my_func = cool()

print(my_func())

# a function that returns a function is known as a higher order function
# here cool is a higher order function that returns the supercool function, 
# which is a nested function. and when we assign the result of cool() to my_func,
# we are actually assigning the supercool function to my_func. so when we call my_func(), 
# it executes the supercool function and returns "super cool".