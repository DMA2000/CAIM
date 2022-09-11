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

def isWord(word):
    dot = False
    number = False
    for letter in word:
        print(letter)
        if letter == '.':
            dot = True
            break
        if letter >= '0' and letter <= '9':
            number = True
            break
    if dot or number: 
        return False
    else:
        return True

news = open ("news_alpha.txt")
lineas = news.readlines()
frequency = getFrequency(lineas[0])
print(frequency)

wold = getWold(lineas[0])
print(wold)
print('Hola')
print(isWord('Hola'))
