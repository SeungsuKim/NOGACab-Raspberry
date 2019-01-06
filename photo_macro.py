from datetime import datetime
import subprocess

from utils import load_yaml_config
from s3_utils import upload_image


if __name__ == "__main__":
    time_setting = load_yaml_config('time_setting.yml')
    time_interval = time_setting.TIME_INTERVAL
    time_last_shot = datetime.now()

    while True:
        if (datetime.now() - time_last_shot).seconds > time_interval:
            # Take a photo and save it with current time.
            imagename = datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + ".jpg"
            imagepath = "images/" + imagename
            result = subprocess.run(['fswebcam', '-r', '1920x1080', imagepath])

            if result.returncode != 0:
                print("Error while taking photo: " + result.stderr)
                time_last_shot = datetime.now()
                break

            # Upload the image to S3 server.
            upload_image(imagepath, "bucket-nogacab/images/" + imagename)

            # Reset the time from last shot.
            time_last_shot = datetime.now()
