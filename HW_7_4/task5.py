import threading, random

shared_lst = []
lock = threading.Lock()


class MyThread(threading.Thread):

    def append_elem(self):
        for _ in range(5):
            num = random.randint(1, 100)
            with lock:
                shared_lst.append(num)
                print(f"Поток {threading.current_thread().name} добавил число {num}. Общий список: {shared_lst}")


def main():
    threads = []
    for i in range(5):
        Thread = MyThread(name=f"Поток{i+1}")
        threads.append(Thread)
        Thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    main()