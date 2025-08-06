with open("D:/Programowanie/Python/logfile.txt", "r", encoding="utf-8") as data_file, open("output.txt", "w", encoding="utf-8") as output_file:
    data = data_file.readlines()
    data = list(map(lambda x: x.strip().split(","), data))
    for i in data:
        i[1] = i[1].strip().split(":")
        i[2] = i[2].strip().split(":")
    for i in data:
        i[1] = int(i[1][0])*60+int(i[1][1])
        i[2] = int(i[2][0])*60+int(i[2][1])
    data = list(filter(lambda x: x[2]-x[1]>=60, data))
    for i in data:
        print(i[0])