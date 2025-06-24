#1.1
def reverse_generator(A, B):
    for num in range(B, A-1, -1):
        yield num

#1.2

def fibonacci_generator():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        if a % 5 == 0:
            yield a

for num in fibonacci_generator():
    if num > 1000:
        break
    print(num)

#1.3

def factorial_generator():
    factor = 1
    count = 1
    while True:
        factor *= count
        yield factor
        count += 1

#1.4 не понял как

#1.5
def unique_generator(text):
    unique_lst = set()
    for word in text:
        if word not in unique_lst:
            unique_lst.add(word)
            yield word

#1.6
def words_generator(text, K):
    for word in text:
        if len(word) > K:
            yield word

#1.7
from itertools import permutations

def character_permutations_generator(string: str, N: int):
    if len(string) == 1:
        yield string

    for c in string:
        for perm in permutations(string.replace(c, '', 1)):
            yield set(perm)

#1.8
def vowels_generator(string):
    vowels = "o", "a", "i", "e"
    unique_lst = set()

    for elem in string:
        if elem in vowels and elem not in unique_lst:
            unique_lst.add(elem)
            yield elem