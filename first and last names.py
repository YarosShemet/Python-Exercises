from random import choice
with open("D:/Programowanie/Python/first_names.txt", encoding='utf-8') as first_name, open("D:/Programowanie/Python/last_names.txt", encoding='utf-8') as last_name:
    first_names = first_name.readlines()
    last_names = last_name.readlines()
    for _ in range(3):
        print(choice(first_names).strip(), choice(last_names).strip())