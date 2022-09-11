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
    badChars = False
    for letter in word:
        if letter == '.':
            dot = True
            #print(letter)
            #print(word)
            break
        if letter >= '0' and letter <= '9':
            number = True
            #print(letter)
            #print(word)
            break
        if not((letter >= "a" and letter <= "z") or (letter == 'æ' or letter == 'þ' or letter == 'ð')):
            badChars == True
            #print(letter)
            #print(word)
            break
    if dot or number or badChars: 
        return False
    else:
        return True

news = open ("news_alpha.txt")
lineas = news.readlines()
#frequency = getFrequency(lineas[0])

#wold = getWold(lineas[0])
#print(wold)
f = open('info.txt', 'w', encoding='utf-8')
for l in lineas:
    freq = l[0]
    w = getWold(l)
    if(isWord(w)):
        f.write(freq)
        f.write(', ')
        f.write(w)
        f.write('\n')
f.close
#if(isWord(wold)) f.write(frequency, ', ', wold)

