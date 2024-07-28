# def sum(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def mul(x, y):
#     return x * y

# def choose_process(func, x, y):
#     return func(x, y)

# print(choose_process(sum, 2, 3)) # sum() etmirik cunki sum() funksiyasini cagirir


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

def square(x):
    return x * x

def cube(x):
    return x * x * x

def calculate(arr, func):
    for i in arr:
        print(func(i))

calculate(arr1, square) # tesevvur edirik ki, 27-ci setirde square(i) olur
calculate(arr1, cube)

print("*********************************************************************************")

calculate(arr2, square)
calculate(arr2, cube)