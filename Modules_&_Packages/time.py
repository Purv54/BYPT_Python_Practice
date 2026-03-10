
from time import time
import timeit

def func1(n):
    return [str(num) for num in range(n)]

def func2(n):
    return list(map(str, range(n)))

# start_time = time()

# func1(10000000)

# end_time = time()

# print(f"Execution time: {end_time - start_time} seconds")

# start_time2 = time()

# func2(10000000)

# end_time2 = time()

# print(f"Execution time: {end_time2 - start_time2} seconds")


# stmt = '''
# func1(100)
# '''

# setup = '''
# def func1(n):
#     return [str(num) for num in range(n)]
# '''

# print(timeit.timeit(stmt, setup, number=1000000))


# stmt2 = '''
# func2(100)
# '''

# setup2 = '''
# def func2(n):
#     return list(map(str, range(n)))
# '''

# print(timeit.timeit(stmt2, setup2, number=1000000))

