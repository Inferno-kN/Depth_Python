import time
import random
import threading


def data():
    print(f"Привет из потока {threading.current_thread().name}.")
    time.sleep(random.randint(1, 3))

def main():
    threads = []
    for _ in range(5, 9):
        Thread = threading.Thread(target=data)
        threads.append(Thread)
        Thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()
