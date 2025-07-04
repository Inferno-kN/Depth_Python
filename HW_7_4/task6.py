import threading

nums = list(range(1, 100))
sums = [0] * 5
threads = []
length = len(nums) // 5


def calculate_sum(start, end, index):
    total = 0
    for i in range(start, end):
        total += nums[i]
    sums[index] = total

for i in range(5):
    start = i * length
    end = length * (i + 1)
    Thread = threading.Thread(target=calculate_sum, args=(start, end, i))
    threads.append(Thread)
    Thread.start()

for thread in threads:
    thread.join()

total_sum = sum(sums)
print(f"Общая сумма: {total_sum}")