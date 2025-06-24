from functools import reduce

#1
for _ in map(lambda str: int(str), ['1', '20', '300']):
    print(_)

#2
for _ in filter(lambda nums: nums % 2 ==0, [1, 2, 3, 4, 5, 6]):
    print(_)

#3
for _ in map(lambda num: num**2, [1, 2, 3, 4]):
    print(_)

#4
for _ in filter(lambda elem: len(elem) > 3, ["cat", "elephant", "dog", "tiger"]):
    print(_)

#5
print(reduce(lambda num1, num2: num1 * num2, [1, 2, 3, 4]))

#6
for _ in map(lambda word: len(word), ["hello", "world", "Python"]):
    print(_)

#7
print(max(map(lambda word: len(word), ["apple", "banana", "pear", "strawberry"])))

#8
for _ in (map(lambda word: word.upper(), ["hello", "world"])):
    print(_)

#9
for _ in filter(lambda num: num % 2 ==0, map(lambda num: int(num)**2, ["1", "2", "3", "4"])):
    print(_)

#10
print(reduce(lambda num1, num2: num1 * num2, filter(lambda num: num >= 0, [-2, 3, -4, 5, 6])))

#11
for _ in map(lambda elem: len(elem), filter(lambda elem: elem[0] in ["a", "e", "i", "o", "u", "y"], ["apple", "banana", "orange", "grape"])):
    print(_)

#12
for _ in filter(lambda elem: elem == elem.reverse(), map(lambda string: [sym for sym in string], ["racecar", "hello", "level", "world"])):
    print(_)

#14
print(reduce(lambda word1, word2: word1 + " " + word2, map(lambda word: word.upper(), filter(lambda string: len(string) % 2 == 0, ["hello", "world", "Python", "is", "great"]))))


#1.1
def generator():
    int_count = 0
    while True:
        int_count += 5
        yield int_count

#1.2
def even_elem():
    square = 1
    while True:
        if isinstance(square, int):
            yield square**2
            square += 1

# 1.3
def return_elem(N: int):
    num = 0
    while num != (N -1):
        num += 1
        if not(num % 3 == 0):
            yield num

#1.5
def plus_elem(A, B):
    while A <= B:
        yield A
        A += 2

#1.6
from random import randint
def random_elem():
    yield randint(1, 100)

#1.7
def fibonacci_generator():
    sequence = [0, 1]
    while True:
        yield sequence[0]
        sequence[0] = sequence[0] + sequence[1]
        yield sequence[1]
        sequence[1] = sequence[0] + sequence[1]


#2.10
def return_day():
    count = 1
    while True:
        yield f"День: {count}"
        count += 1