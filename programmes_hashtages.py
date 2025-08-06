with open("D:/Programowanie/Python/hashtag.txt", "r", encoding="utf-8") as file:
    code = file.readlines()
    def_code = list(filter(lambda x: x.strip().startswith("def"), code))
    new_list = []
    result = []
    for i in range(1, len(code)+1):
        if code[i-1][0] == "#":
            new_list.append(code[i])
    for func in def_code:
        if func not in new_list:
            result.append(func[4:func.index("(")])
    if result == []:
        print("Best Programming Team")
    else:
        print(*result, sep="\n")
