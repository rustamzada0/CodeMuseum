# def func(x):
#     return x * x

# a = func(3)
# print(a)

# b = func
# print(b)
# print(b(3))


# def choose_process(process):
#     def sum(*args):
#         result = 0
#         for arg in args:
#             result += arg
#         print(result)
    
#     def multiply(*args):
#         result = 1
#         for arg in args:
#             result *= arg
#         print(result)
    
#     if process == "sum":
#         return sum
#     elif process == "multiply":
#         return multiply
#     else:
#         return "Invalid process"
    
# choose_process("sum")(1, 2, 3, 4, 5)


# def choose_person(person):
#     def choose_club(club):
#         return f"{person} favorite club is {club}"

#     return choose_club

# a = choose_person("John")
# b = choose_person("Jane")

# print(a("Manchester United"))
# print(b("Chelsea"))