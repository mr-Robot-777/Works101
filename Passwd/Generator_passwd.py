# Вариант 1

import random
from string import digits
from string import punctuation
from string import ascii_letters

# log = int(input('Введите длинну логина : '))
# pasw = int(input('Введите длинну пароля: '))
# symbols = ascii_letters + digits + punctuation
# secure_random = random.SystemRandom()
# login = "".join(secure_random.choice(ascii_letters) for i in range(log))
# password = "".join(secure_random.choice(symbols) for j in range(pasw))
#
# print("--------------------------------------------------")
# print("Ваш логин: ", login)
# print("--------------------------------------------------")
# print("Ваш пароль: ", password)
# print("--------------------------------------------------")



# Вариант 2


import random
passwd = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" #[]{}()*;:/,_-%№@$!#=+^&<>"
length = int(input("\nВведите длину пароля (до 87 символов): "))
password = "".join(random.sample(passwd, length))

print("--------------------------------------------------")
print("Ваш пароль: ", password)
print("--------------------------------------------------")


# Вариант 3


# import random
# upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lower = "abcdefghijklmnopqrstuvwxyz"
# numbers = "0123456789"
# symbol = "[]{}()*;:/,_-%№@$!#=+^&<>"
#
# login = upper + lower + numbers
# passwd = upper + lower + numbers + symbol
#
# length_log = int(input("\nВведите длину Логина (до   62  символов): "))
# length_pass = int(input("Введите длину Пароля (до  87   символов): "))
#
# login =  "".join(random.sample(login, length_log))
# password = "".join(random.sample(passwd, length_pass))
#
# print("--------------------------------------------------")
# print("Ваш  логин: ", login)
# print("Ваш пароль: ", password)
# print("--------------------------------------------------")

