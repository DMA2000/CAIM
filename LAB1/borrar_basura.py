# esto
# Prueba de push

def getFrequency (line):
    frequency = line[0];
    for i in range(1, len(line)):
        if line[i] != ',':
            frequency = frequency + line[i]
        else:
            break;
    return int(frequency)

def getWold (line):
    word = ""
    i = 0;
    while i < len(line):
        if (line[i] == ','):
            break;
        i = i +1;
    i += 2;
    while i < len(line):
        word = word + line[i];
        i = i + 1;
    return word


news = open ("news_alpha.txt")
lineas = news.readlines()
frequency = getFrequency(lineas[0])
print(frequency)

wold = getWold(lineas[0])
print(wold)
