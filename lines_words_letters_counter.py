with open("...", encoding='utf-8') as file:
    list_of_sentences = file.readlines()
    lines_cnt = len(list_of_sentences)
    word_cnt = 0
    letters_cnt = 0
    for line in list_of_sentences:
        word_cnt += len(line.split())
        for symbol in line:
            if symbol.isalpha():
                letters_cnt += 1
    print("Input file contains:", str(letters_cnt) + " letters", str(word_cnt) + " words", str(lines_cnt) + " lines", sep="\n")