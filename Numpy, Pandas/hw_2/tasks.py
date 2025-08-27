import numpy as np
from matplotlib import pyplot as plt

# alcohol,volatile acidity,sulphates,pH,quality
dataset = np.loadtxt(
"wine_quality.csv",
delimiter=",",
skiprows=1)


#1
print(np.mean(dataset, axis=0))
print(np.median(dataset, axis=0))
print(np.var(dataset, axis=0))
print(np.min(dataset, axis=0))
print(np.max(dataset, axis=0))

#2
max_quality = np.max(dataset[:, -1], axis=0)
records = dataset[dataset[:, -1] == max_quality]
pH = np.mean(records[:, 3])
print(pH)

#3
quality = dataset[:, -1]
maxx_quality = np.max(quality, axis=0)
minn_quality = np.min(quality, axis=0)
quality =- minn_quality
range_quality = maxx_quality - minn_quality
quality = quality / range_quality
print(quality)

#ЗАДАЧИ НА ВИЗУАЛИЗАЦИЮ

#1
quality = dataset[:, -1]
qualities, counts = np.unique(quality, return_counts=True)

plt.bar(qualities, counts)
plt.xlabel('Уровень качества')
plt.ylabel('Количество записей')
plt.title('Распределение уровней качества')
plt.show()

#2
max1_quality = np.max(quality, axis=0)
min1_quality = np.min(quality, axis=0)

low_quality = quality == min1_quality
high_quality = quality == max1_quality

plt.scatter(dataset[low_quality, 2], dataset[low_quality, 1], color="green", label="Низкое качество")
plt.scatter(dataset[high_quality, 2], dataset[high_quality, 1], color="orange", label="Высокое качество")
plt.xlabel('volatile acidity')
plt.ylabel('alcohol')
plt.title('Зависимость между летучей кислотой и обьемом спирта')
plt.show()
