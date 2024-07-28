# def my_decorator(func):
#     def wrapper():
#         print("Before function call")
#         func()
#         print("After function call")
#     return wrapper

# # 1-ci versiya (decorator annotationlu )
# # @my_decorator
# def my_function():
#     print("Hello, World!")

# # my_function()

# # 2-ci versiya (@ decorator annotationsuz )
# # x = my_decorator(my_function)
# # x()


import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} is executed in {end_time - start_time}")
    
    return wrapper

@calculate_time
def square(arr):
    for i in arr:
        print(i * i)

def cube(arr):
    for i in arr:
        print(i * i * i)

# square(range(1, 1000000))

z = calculate_time(cube) # z = wrapper - dir
z(range(1, 1000000)) # wrapper(range(1, 1000000)) edirik