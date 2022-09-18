from traceback import print_last


def getFrequency (line):
    frequency = line[0];
    for i in range(1, len(line)):
        if line[i] != ' ':
            frequency = frequency + line[i]
        else:
            break
    return int(frequency)

text = open("info_novels.txt")
lineas = text.readlines()

total = len(lineas)
difWords = 0
nWords = 0
for l in range (0, total):
        nWords += getFrequency(lineas[l])
        difWords += 1

print("Número total de palabras ", nWords, "\nNúmero de palabras diferentes ", difWords)

