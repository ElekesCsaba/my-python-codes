import random, time
from utilities.decorators import timer, logger


@timer
@logger
def worker1(sleep_time):
    print("Worker1 started...")
    time.sleep(sleep_time)
    print("Worker1 ended.")


@timer
def worker2():
    print("Start2")
    time.sleep(random.randint(3, 10))
    print("End2")


@timer
def worker3(name):
    print("Start3")
    time.sleep(random.randint(3, 10))
    print("End3")


worker1(3)
