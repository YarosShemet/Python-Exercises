with open("forbidden_words.txt", "r", encoding="utf-8") as forb_words, open(input(), "r+", encoding="utf-8") as write_file:
    forbidden_words = forb_words.read().split()
    pre_text = write_file.read()
    text = pre_text.lower()
    for word in forbidden_words:
        while word in text:
            text = text.replace(word, "*" * len(word))
    result = ""
    for i in range(len(text)):
        if text[i] == '*':
            result += '*'
        else:
            result += pre_text[i]
    print(result)



