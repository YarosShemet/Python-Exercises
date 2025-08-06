genome = input()
genome = genome.upper()
g = "G"
c = "C"
d = genome.count(g)
f = genome.count(c)
print(((d + f) / len(genome)) * 100)


