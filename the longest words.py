with open("D:/Programowanie/Python/words.txt", "r", encoding="utf-8") as file:
    data = file.read().split()
    data = list(filter(lambda x: len(x)==len(sorted(data, key=len)[-1]), data))
    print(*data,sep="\n")