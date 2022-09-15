import matplotlib.pyplot as plt


def getFrequency (line):
    frequency = line[0];
    for i in range(1, len(line)):
        frequency = frequency + line[i]
    return int(frequency)

news = open ("info.txt")
lineas = news.readlines()
f = open('test.txt', 'w', encoding='utf-8')
total = len(lineas)

array = []
for l in range (0, total):
    array.append( getFrequency(lineas[l]) )


#test array
#for l in range(0, total):
#    f.write(str(array[l]))
#    f.write('\n')

plt.plot(array)
plt.yscale('log')
plt.ylabel('frecuency')
plt.xlabel('rank')
plt.xscale('log')
plt.show()


