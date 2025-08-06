from random import choice
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
number = int(input("Сколько паролей требуется? "))
length = int(input("Сколько символов нужно для пароля? "))
need_digit = input("Нужны ли цифры в пароле? ")
need_upper = input("Нужны ли большие буквы? ")
need_lower = input("Нужны ли маленькие буквы? ")
need_symbols = input("Нужны ли специальные символы? ")
exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')
if need_digit.lower() == "да":
    chars += digits
if need_upper.lower() == "да":
    chars += uppercase_letters
if need_lower.lower() == "да":
    chars += lowercase_letters
if need_symbols.lower() == "да":
    chars += punctuation
if exceptions.lower() == "да":
    for i in chars:
        if i in "il1Lo0O":
            chars = chars.replace(i, "")
def generate_password(length, chars):
    password = ""
    for i in range(length):
        password += choice(chars)
    return password
print("Сохраняй себе!")
for _ in range(number):
    print(generate_password(length, chars))



