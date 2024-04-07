import os 
import shutil
import time

TEMP_DIR= "D:\\Workspace\\DATN\\backend-py\\temp"
os.makedirs(TEMP_DIR, exist_ok=True)

def save_fastapi_request_file(url_file):
    filename = url_file.filename
    extension = filename[filename.rfind('.'):].lower()

    timestamp = time.time_ns()
    image_file = os.path.join(TEMP_DIR, f'{timestamp}{extension}')
    if os.path.isfile(image_file):
        timestamp += 1
        image_file = os.path.join(TEMP_DIR, f'{timestamp}{extension}')
    with open(image_file, "wb") as buffer:
        shutil.copyfileobj(url_file.file, buffer)

    return image_file

def delete_file(filepath):
    if filepath is not None and (os.path.isfile(filepath) or os.path.islink(filepath)):
        os.unlink(filepath)