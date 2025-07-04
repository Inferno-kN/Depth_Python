import threading
import time
import random


class MyThread(threading.Thread):
    def __init__(self, name: str, delay: int or float):
        super().__init__()
        self.__name = name
        self.__delay = delay

    def get_delay(self):
        return self.__delay

    def data(self):
        print(f"Поток {threading.current_thread().name} начался")
        time.sleep(self.get_delay())
        print(f"Потом {threading.current_thread().name} завершён")

def main():
    threads = []
    for _ in range(7):
        name = threading.current_thread().name
        delay = time.sleep(random.randint(1, 3))
        Thread = MyThread(name, delay)
        threads.append(Thread)
        Thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()





