import s3fs
from utils import load_yaml_config


# Returns a s3 file object.
def get_s3fs():
    certificate = load_yaml_config('certificate.yml')
    aws_access_id = certificate.AWS_ACCESS_ID
    aws_secret_key = certificate.AWS_SECRET_KEY
    fs = s3fs.S3FileSystem(key=aws_access_id, secret=aws_secret_key)
    return fs


def upload_image(imagepath, filepath):
    fs = get_s3fs()
    with fs.open(filepath, 'wb') as fw:
        with open(imagepath, 'rb') as fr:
            imagedata = fr.read()
        fw.write(imagedata)


if __name__ == '__main__':
    upload_image("images/sample_image.jpg", "bucket-nogacab/sample_image.jpg")