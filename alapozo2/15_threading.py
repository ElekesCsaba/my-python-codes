import time, threading


def worker1(sleep_time):
    print("Started1.")
    time.sleep(sleep_time)
    print("Ended1.")


def worker2(sleep_time):
    print("Started2.")
    time.sleep(sleep_time)
    print("Ended2.")


t1 = threading.Thread(target=worker1, args=[3])
t2 = threading.Thread(target=worker2, args=[6])

t1.start()
t2.start()
