# problem 3:
q = (17391/17)
print (q)
w = (546/17)
print(w)
e = (934/17)
print(e)

if w < e:
    print("w меньше остатка чем у e")



 


# problem 4:
x = (13**2)
print(x)
c = 172
print(c)
if x == c:
    print("x равна c")
elif c == x:
    print("c равна x")
else:
    print("x меньше c")



# problem 5:
www = (99/2)
print(www)
vvv = (99/3)
print(vvv)
ggg = (vvv**2)
print(ggg)
if ggg > 1000:
    print("ggg больше чем 1000")#



# problem 6:
number = 0
if number > 20 and number < 21:
    print("от 100 отнимаем 20")
elif number > 57 and number > 100:
    print("и отнимаем с 57 до 101")
elif 20 > number and 57 == 100:
    print("верный ли ответ") 
else:
    print("от 21 до 57 считаются запрещенными числами")


# problem 7:
you = 18
to_me = 17
if you < to_me:
    print("vsvsvs")
elif you == to_me:
    print("UFS UFS")
else:
    print("не имеет значение")



# problem 8:
visa = int(input("ваш возраст?:"))
if visa >=14:
    print("ваш возраст 17")
else:
    if visa ==24:
        print("точно, ваш возраст 17") 
    else:
        if visa >=19:
            print("окей, ваш возраст 17")
        else:
            if visa <=36:
                print("ладно ваш возраст 17")
            else:
                print("мне 17 лет!")


a = 10//5
print(a)
b = 10/5
print(b)
if a > b:
    print("a больше b")
elif b > a:
    print("b  больше a")
elif a < b:
    print("a меньше b")
else:
    print("a и b равны")



a = int(input("ваше число"))
if a > 0:
    print("отрицательное число 1")
elif a > 3:
    print("отрицательное число 2")
else:
    print("отрицательные числa -")  


a = 10
b = 5
if a > 0 and b > 0:
    print("является положительным!")

a = 10
b = 5
if a > b:
    print(a + 2)
else:
    print(b + 2)

for i in range(1, 10):
    if i == 5:
        print(i)
    else:
        print("Number not found")

a = 5
while  a < 15:
    print(a)
    a = a + 1
    

for i in range(1,1000):
    if i % 7 == 0:
        print(i)


a = 'absdifgghjgjhgjhglgh'
for h , f in enumerate(a):
    print(h, f)



energy = 1000

sport = 100


user_active = int(input("Напишите что вы хотите делать? "))

if user_active == 1:
    result = energy - sport
    print(result, "Осталось энергии")




energy = 1000

sport = 100
home_activity = 60
lessons = 180
listen_to_whining = 200

music = 60
meal = 150
dream = 500







energy = 1000

sport = 100
home_activity = 60
lessons = 180
listen_to_whining = 200





user = int(input("выберите активности!"))
if user ==1:
    result = energy - sport 
    print(result,"energy left")


user2 =int(input("выберите активность 2!"))    
if user2 ==2:
        result22 = result - home_activity 
        print(result22, "energy left")

user3 = int(input("выберите активность 3!"))
if user3 ==3:
      result33 = result22 - lessons 
      print(result33,"energy left")
    

user4 = int(input("выберите активность4!"))
if user4 ==4:
      result44 = result33 - listen_to_whining 
      print(result44,"energy left")

user5 = int(input("выберите активность 5!"))
if user5 ==5:
      result55 = result44 - sport 
      print(result55,"energy left")

user6 = int(input("выберите активность 6!"))
if user6 ==6:
      result66 = result55 - home_activity 
      print(result66, "energy left")

user7 = int(input("выберите активность 7!"))
if user7 ==7:
      result77 = result66 - lessons 
      print(result77,"energy left")

user8 = int(input("выберите активности 8!"))
if user8 ==8:
      result88 = result77 - home_activity
      print(result88,"energy left")

user9 = int(input("выберите активность 9!"))
if user9 ==9:
      result99 = result88 - home_activity
      print(result99, "energy left")



music = 60
meal = 150
dream = 500

while music < dream:
    print(music)
    
















