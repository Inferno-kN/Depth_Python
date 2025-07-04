import time, random, threading


class MyThread(threading.Thread):
    def __init__(self, sleep):
        super().__init__()
        self.sleep = sleep

    def run(self):
        print(f"Поток {threading.current_thread().name} работает")
        time.sleep(self.sleep)


def main():
    threads = []
    for _ in range(5, 11):
        sleep_time = random.randint(5, 10)
        Thread = MyThread(sleep_time)
        threads.append(Thread)
        Thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()





