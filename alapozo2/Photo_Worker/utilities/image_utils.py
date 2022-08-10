from PIL import Image, ExifTags
import os, threading, queue


def create_thumbnails(file_list: list, thumbnail_folder: str, thumb_size=300) -> None:

    # Define queue.
    job_queue = queue.Queue()

    # Load files into queue.
    job_queue = update_queue(job_queue, file_list)

    # Start threads for resizing.
    spawn_photo_workers(job_queue, thumbnail_folder, thumb_size, 8)


def spawn_photo_workers(job_queue: queue, thumbnail_folder: str, thumb_size: int, worker_number: int) -> None:

    # Spawning threads.
    for _ in range(worker_number):
        t = threading.Thread(target=photo_worker, args=[job_queue, thumbnail_folder, thumb_size])
        t.start()


def photo_worker(job_queue: queue, thumbnail_folder: str, thumb_size) -> None:

    # Converting files in queue.
    while not job_queue.empty():
        photo_file = job_queue.get()

        img = Image.open(photo_file)
        img.thumbnail((thumb_size, thumb_size))
        img.save(os.path.join(thumbnail_folder, os.path.basename(photo_file)))

        job_queue.task_done()


def update_queue(job_queue: queue, file_list: list) -> queue:

    # Put files into queue.
    for i in file_list:
        job_queue.put(i)

    return job_queue


def create_image_dict(file_list: list) -> dict:

    photo_data = {}

    for file_path in file_list:
        img = Image.open(file_path)
        file_name = os.path.basename(file_path)

        photo_data[file_name] = {
            "x": img.size[0],
            "y": img.size[1],
            "path": file_path,
            "date": None,
            "camera": None,
            "iso": None
        }

        # Get exif data.
        exif_data = img._getexif()
        if not exif_data:
            continue

        # Load some ExifTag values into dictionary.
        for key, value in exif_data.items():
            tag_name = ExifTags.TAGS.get(key)

            match tag_name:
                case "DateTimeOriginal":
                    photo_data[file_name]["date"] = value
                case "Model":
                    photo_data[file_name]["camera"] = value
                case "ISOSpeedRatings":
                    photo_data[file_name]["iso"] = value
                case _:
                    continue

    return photo_data
