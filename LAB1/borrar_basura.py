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



news = open ("news_alpha.txt")
lineas = news.readlines()
for i in range (0, len(lineas)-1):
    print(1)
