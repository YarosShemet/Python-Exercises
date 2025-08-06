d = {
    'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch',
    'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*',
    'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je',
    'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya'
    }
with open("D:/Programowanie/Python/cyrillic.txt", "r", encoding="utf-8") as input_file, open("transliteration.txt", "w", encoding="utf-8") as output_file:
    data = input_file.readlines()
    new_string = ""
    for word in data:
        for i in range(len(word)):
            if word[i].lower() in d.keys():
                if word[i].isupper():
                    new_string += d[word[i].lower()].capitalize()
                else:
                    new_string += d[word[i]]
            else:
                new_string += word[i]
        if word.endswith(".\n")==False:
            new_string += " "
    print(new_string)