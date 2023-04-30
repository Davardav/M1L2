import random
simvol = '+-/*abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
dlina = int(input('количество символов в пароле:' ))
password = ''
for i in range(dlina):
    password += random.choice(simvol)
print(password)