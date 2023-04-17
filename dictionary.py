#1
#  menu = {'lagman': '120',
# 'plov' : '120', 
# 'borsh': '100'}

# menu['drinks'] = 'Coca-Cola, fanta, sprine'
# print(menu) 

# 2

# name = {}

# for i in range(1,4):
        
#         x = input("введите имя")
#         d = input("введите пароль")

# name.update({"aika":"you"})
# print(name)

# 3 
# prof = {'врач':'медик',
#         'профессор':'учитель',
#         'мафия':'лидер',
#         'депутат':'пустышка',
#         'дипломат':'переводчик'}

# for i in range(1,2):
#     w = input("Здравствуйте")
#     q = input("прекрасная профессия")



menu = {'lagman': 120, 'plov': 120, 'borsh': 100}

menu.update({"besh_barmak":135})
print(menu)

menu.update({'lagman':135})
print(menu)

# menu.clear()
# print(menu)

# menu.get({'lagman','plov','Argentina'})
# print(menu)

menu.pop("borsh")
print(menu)


# america = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'chile','Argentina']
# america.remove("Argentina")
# print(america)

# menu.update({'Argentina':6})
# print(menu)



import random
print({random.randint(3,14) for x in random})
