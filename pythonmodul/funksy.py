# 1 задание
# def func(first_name,last_name ):
#     return f" {first_name} {last_name}"
# print(func("крот","кротов"))


# 2 задание
# def userstr(str = "sakura,sakura,19,18,19"):
#     str == set()
#     return True
# print(userstr("sakura,sakura,19,18,19"))

# 3 задание
# def function(name_pokemon,level_pokemon,type_pokemon):
#     return f"{name_pokemon} level_pokemon {level_pokemon}{type_pokemon}"
# print(function("Pikachu", 10, " Electro"))

# 4 задание 
# def name(*chisla):
#     i = list(chisla)
#     return i
# name(1,2,3,4,5,6,7,8,9,10)
# w = tuple(range(10,11))
# q = tuple(range(1,2))
# print(w,q)












# def name():
#     print("hello")
#     print("bitch")

# def hello(x):
#     print('квадрат числа',x,"=",x**2)

# for i in range(1,11): (11 не включительна)
    # hello(i)


# hello(10)

# name()
# print("please")
# name()
    

# def please(a,b):
#     print(a*b)


# please(5,8)
# please(20,70)

# def even(a):
#     if a%10==0:
#         print(a,"ваше число четное")
#     else:
#         print("теперь не четное!")

# even(20)
# even(33)
            # 7
# def factorial(n):
#     pr=1
#                   #  7  
#     for i in range(2,n+1):
#         pr=pr*i
#     print(pr)

# factorial(7)



# def shop(**kwargs):
#     for kw in kwargs:
#         result  = kw, ":", kwargs[kw]
#         return result
        

# print(shop(frukty=["Бананы", 'Яблоки', "Грушы"]), )
# print(shop(car=["Мерседес", " BMW"]))
# print(shop(ovoshi=["Картоха", "Марковка","Лук"]))



# def printNames(owner, **kwargs):
#     print(f"Имя владельца: {owner}")

#     for keys, values in kwargs.items():
#         print(f"{keys}: {values}")

# printNames("Bob", game="SEGA", dog="MOPS", fish=["Larry"])



# метод *
# def userstr(*ris):
#     return ris
# print(userstr(12,34,56))