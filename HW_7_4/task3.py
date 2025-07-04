import threading

count = 0

def add_element():
    global count
    count += 1
    return count

def main():
    threads = []
    for _ in range(50):
        Thread = threading.Thread(target=add_element)
        threads.append(Thread)
        Thread.start()


    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
