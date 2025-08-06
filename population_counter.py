with open("D:/Programowanie/Python/data.csv", encoding="utf-8") as file:
    data = file.readlines()
    data = [x.strip().split(",") for x in data]
    keys = data[0]
    result = []
    for j in range(1, len(data[1:])+1):
        read_csv = {}
        for i in range(len(keys)):
            line = data[j]
            read_csv[keys[i]] = line[i]
        result.append(read_csv)
print(result)