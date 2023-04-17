www_password = input("введите имя пользователя:")
qqq_login = input("введите пароль:")
print

with open('file.txt',"a")as dog:
    dog.wrire(www_password)

file_x = open("file.txt","a")
fail_gg = file_x.write()
print(fail_gg)