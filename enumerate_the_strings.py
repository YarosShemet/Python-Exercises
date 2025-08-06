with open("D:/Programowanie/Python/input.txt", "r", encoding="utf-8") as input_file:
    data = list(enumerate(input_file.readlines(), 1))
    with open("output.txt", "w", encoding="utf-8") as output_file:
        for pair in data:
            print(str(pair[0])+") "+pair[1], end="")