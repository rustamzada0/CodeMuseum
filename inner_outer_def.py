# def outer():
#     print("Outer function started")
#     def inner():
#         print("Inner function")

#     print("Outer function ended")
#     return inner()

# my_func = outer()


# def calculate(arg, x):
#     def square(x):
#         print(x * x)

#     def cube(x):
#         print(x * x * x)

#     if arg == "square":
#         return square 
#     elif arg == "cube":
#         cube(x) 
#     else:
#         print("Invalid input")

# calculate("cube", 3) #27 verecek cunki ilk once calculate funskiyasi cagrilacag ve "cube" oldugu ucun elif ishleyecek ve sade bir mentigle cube() funksiyasi ÇAĞRILACAQ

# calculate("square", 3) # burada "square" olduqu ucun if ishleyecek ve square funksiyasi Return olacaq (qaytarilacaq yeni cagrilmiyacaq) ve bunu istesez bir variableye menimsede bilerik (funksiya ram adress) yeni ozu bir funksiya olacaq yene
# calculate("square", 2)(2) # bir funskiya oduqu ucun (2) yazilacaq "Birinci morterizedeki ("square", "2")"-deki "2"-nin bir meqsedi yoxdur (missing olmasin deyedir)


def calculate(x):
    def square(a):
        return a ** 2
    def cube(a):
        return a ** 3
    def factorial(a):
        fact = 1
        for i in range(1, a+1):
            fact *= i
        return fact
    
    square = square(x)
    cube = cube(x)
    factorial = factorial(x)

    print(square, cube, factorial)

calculate(5)