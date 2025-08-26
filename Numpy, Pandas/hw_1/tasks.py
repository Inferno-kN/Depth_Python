import numpy as np

#1
temps = np.array([15.2, 16.8, 14.5, 17.0, 16.1])

print(np.sum(temps))
print(np.mean(temps))
print(np.min(temps))
print(np.max(temps))

#2
h1 = np.array([45, 50, 47])
h2 = np.array([48, 46, 52])

print(h1 + h2)
print(h1 * h2)
print(np.dot(h1, h2))

#3
X = np.array([
 [20.1, 20.3, 19.8],
 [21.0, 20.7, 20.2],
 [19.5, 19.8, 19.3],
 [20.8, 21.1, 20.6]
 ])

print(np.mean(X, axis=0))
print(np.sum(X, axis=1))
print(np.var(X, axis=0, ddof=1))
print(np.argmin(np.var(X, axis=0)))

#4
X = np.array([
[20.1, 20.3, 19.8],
[21.0, 20.7, 20.2],
[19.5, 19.8, 19.3],
[20.8, 21.1, 20.6]
])

col_min = np.min(X, axis=0)
col_max = np.max(X, axis=0)
col_range = col_max - col_min
print(col_min, col_max)
print(col_range)

#5
ph = np.array([
[7.1, 7.4, 7.0],
[6.9, 7.2, 7.1],
[7.3, 7.5, 7.2],
[7.0, 7.1, 6.8],
[6.8, 6.9, 6.7],
[7.4, 7.6, 7.3]
])

print(np.mean(ph, axis=1))
print(np.sum(ph, axis=0))
print(np.sum(ph, axis=1))
print(np.var(ph, axis=0))

#6
consumption = np.array([
[ 8, 6, 5], # Mon
[10, 7, 6], # Tue
[ 9, 8, 7], # Wed
[11, 10, 9], # Thu
[14, 12, 11], # Fri
[16, 15, 13], # Sat
[12, 11, 10] # Sun
])
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
houses = ['H1','H2','H3']

print(np.sum(consumption, axis=0))
print(np.sum(consumption, axis=1))
print(np.mean(consumption, axis=0))
print(days[np.argmax(np.sum(consumption, axis=1))])
print(np.var(consumption, axis=0, ddof=1))

#7
sensors = np.array([
[15, 101, 20, 0.5],
[16, 100, 21, 0.6],
[15, 102, 19, 0.4],
[17, 103, 22, 0.7],
[18, 104, 23, 0.6],
[19, 105, 24, 0.8],
[17, 103, 22, 0.5]
])
types = ['TempSensor','PressureSensor','FlowSensor','VibrationSensor']

print(np.sum(sensors, axis=0))
print(np.mean(sensors, axis=1))
print(np.var(sensors, axis=0, ddof=1))