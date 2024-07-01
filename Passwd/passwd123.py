# # def shift(word, key):
# #     counter = 0
# #     result = ''
# #     letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
# #
# #     for letter in word:
# #         if counter > len(key) - 1:
# #             counter = 0
# #
# #         if letter in letters:
# #             result += letters[letters.index(letter) + int(key[counter])]
# #             counter += 1
# #
# #         else:
# #             result += letter
# #             counter += 1
# #
# #     return result
# #
# # print(shift("наполеон",3))
#
#
# # def main():
# #     import string
# #     import re
# #     alph = string.ascii_lowercase
# #     cd = 'aaaaabbbbbabbbaabbababbaaababaab'
# #     mes = input().replace(' ', '')
# #     decod = {cd[i:i + 5]: alph[i] for i in range(26)}
# #     mes = re.sub(r'([A-Z])', 'b', re.sub(r'([a-z])', 'a', mes))
# #     res = ''
# #     for i in range(0, len(mes) // 5 * 5, 5):
# #         res += decod[mes[i:i + 5]]
# #     return res
# #
# #
# # print(main())
#
#
#
# from random import randint
#
# mass = []
# any_str = str(input("Input any string you want: "))
#
# for i in  any_str:
#  mass.append(i)
#
# print("")
# print(mass)
#
# mass2 = []
#
# j = randint(0,len(mass))
#
# for k in mass:
#  mass2.append(mass[j])
#  j = randint(0,len(mass))
#
# print(mass2)


import random, easygui

secret = random.randint(1, 99)
guess = 0
tries = 0
easygui.msgbox("""AHOY! I'm the Dread Pirate Roberts,
and I have a secret!
Графические интерфейсы пользователя
 77
It is a number from 1 to 99. I'll give you 6 tries.""")

while guess != secret and tries < 6:
    guess = easygui.integerbox("What's yer guess, matey?")
    if not guess: break

    if guess < secret:

        easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
    elif guess > secret:
        easygui.msgbox(str(guess) + " is too high, landlubber!")
        tries = tries + 1
if guess == secret:
    easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
else:
    easygui.msgbox("No more guesses! The number was " + str(secret))
