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
def load_yaml_config(filename):
    with open(filename, 'r') as stream:
        try:
            return ObjDict(yaml.load(stream))
        except yaml.YAMLError as _:
            return None