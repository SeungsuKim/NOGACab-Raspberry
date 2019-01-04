import s3fs
import yaml

# A dictionary object which value can be access with dot notation.
class ObjDict(dict):

    def __getattr__(self, key):
        if key in self:
            return self[key]
        else:
            raise AttributeError("No such key: " + key)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        if key in self:
            del self[key]
        else:
            raise AttributeError("No such key: " + key)


# Returns a ObjDict object containing certificate.
def load_yaml_config(filename="certificate.yml"):
    with open(filename, 'r') as stream:
        try:
            return ObjDict(yaml.load(stream))
        except yaml.YAMLError as _:
            return None


# Returns a s3 file object.
def get_s3fs():
    certificate = load_yaml_config()
    aws_access_id = certificate.AWS_ACCESS_ID
    aws_secret_key = certificate.AWS_SECRET_KEY
    fs = s3fs.S3FileSystem(key=aws_access_id, secret=aws_secret_key)
    return fs


def upload_image(imagename, filepath):
    fs = get_s3fs()
    with fs.open(filepath, 'wb') as fw:
        imagepath = "./images/" + imagename
        with open(imagepath, 'rb') as fr:
            imagedata = fr.read()
        fw.write(imagedata)


if __name__ == '__main__':
    upload_image("sample_image.jpg", "bucket-nogacab/sample_image.jpg")