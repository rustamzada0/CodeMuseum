#####################################################################
    # class MyClass1:
    #     pass


    # class MyClass2(MyClass1):
    #     pass

    # obj = MyClass1()
    # print(isinstance(obj, MyClass1))  # True
    # print(issubclass(MyClass2, MyClass1)) # True
#####################################################################


# python her bir data type (str,int,float,bool,list,tuple,dict,set) öz-özlüyündə bir class həm də data type dir və həm də hamısı type class-ının obyektidir.
# burdan bele neticeye gelirik ki, butun data type-ler type class-inin obyektidir ama object class-inin hem obyekti hem de subclass-dir
print(isinstance(list, type)) # True
print(issubclass(list, type))  # False (yeniki list classi type classinin subclass-i deyil instance-dir)

print(isinstance(list, object)) # True
print(issubclass(list, object))  # True


# butun data type obyektleri oz class-inin ve object class-inin obyektidir
print(isinstance(5, int)) # True
print(isinstance(5, object)) # True
print(isinstance(5, type)) # False


# type classi ozu ozunun ve object classinin hem subclassi hem de instancedir
print(isinstance(type, type)) # True
print(issubclass(type, type))  # True

print(isinstance(type, object)) # True
print(issubclass(type, object)) # True

# ama object classi type-in subclassi deyil yalniz instancedir
print(isinstance(object, type)) # True
print(issubclass(object, type)) # False

# object classi da ozu ozunun hem subclassi hem de instancedir
print(isinstance(object, object)) # True
print(issubclass(object, object)) # True