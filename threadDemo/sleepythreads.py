import random, time
from threading import Thread


class SleepyThread(Thread):
    def __init__(self, number, sleep_max):
        Thread.__init__(self, name='Thread ' + str(number))
        self._sleepInterval = random.randint(1, sleep_max)

    def run(self):
        print('%s, sleep interval: %d seconds' % (self.getName(), self._sleepInterval))
        time.sleep(self._sleepInterval)
        print('%s waking up' % self.getName())


def main():
    num_threads = input('Enter the number of threads: ')
    sleep_max = input('Enter the maximum sleep time: ')
    thread_list = []
    num_threads = int(num_threads)
    sleep_max = int(sleep_max)
    for count in range(num_threads):
        thread_list.append(SleepyThread(count + 1, sleep_max))
    for thread in thread_list:
        thread.start()


main()
