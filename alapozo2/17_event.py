import time, threading

# jelzőlámpa
downloading = threading.Event()


def download_worker():
    downloading.clear()

    print("Downloading started.")
    time.sleep(3)
    print("Downloading finished.")
    downloading.set()


def file_converter_worker():
    downloading.wait()

    print("Converter started.")
    time.sleep(3)
    print("Converter finished.")


t1 = threading.Thread(target=download_worker)
t2 = threading.Thread(target=file_converter_worker)

t1.start()
t2.start()
