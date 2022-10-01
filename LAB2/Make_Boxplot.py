#import seaborn as sns
#import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
array = []

results = open ("test.txt")
lineas = results.readlines()
total = len(lineas)
#print(lineas)
for value in lineas:
    array.append(float(value))

#d = {'Valores': array}
#df = pd.DataFrame(data=d)
#print(type(array[0]))
#sns.boxplot(x = df['Valores']).imshow()

plt.boxplot(array)
plt.show()