from utilities.file_utils import get_files
import time, random, threading, queue

# create queue
job_queue = queue.Queue()

# standard python list is not good for threading
files = get_files(r"C:\Work\PythonSuli\pycore-220108\kepek")


# add files to queue
for i in files:
    job_queue.put(i)


def file_worker():
    while not job_queue.empty():
        next_job = job_queue.get()
        print(f"{threading.current_thread().name}: Working with: {next_job}.")

        time.sleep(random.randint(1, 3))

        print(f"{threading.current_thread().name}: Finished with {next_job}.")

        job_queue.task_done()


for _ in range(8):
    t = threading.Thread(target=file_worker)
    t.start()
