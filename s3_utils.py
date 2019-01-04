import s3fs
import yaml


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


def load_yaml_config(filename="certificates.")