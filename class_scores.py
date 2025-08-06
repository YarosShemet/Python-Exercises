with open("D:/Programowanie/Python/class_scores.txt", "r", encoding="utf-8") as input_file:
    with open("new_scores.txt", "w", encoding="utf-8") as output_file:
        old_scores = input_file.readlines()
        old_scores = list(map(lambda x: x.split(), old_scores))
        for i in old_scores:
            if int(i[1])+5 > 100:
                i[1] = "100"
            else:
                i[1] = str(int(i[1])+5)
            print(((i[0]+" "+i[1])))