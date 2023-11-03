import yaml
import os


class Config(object):
    def __init__(self, path="config.yaml"):
        with open(path) as file:
            self.config = yaml.load(file, Loader=yaml.FullLoader)

    def get_by_name(self, name: str):
        names = name.split(".")
        d = self.config
        for name in names:
            if name not in d:
                return None
            d = d[name]
            if not isinstance(d, dict):
                return d
        return None


conf = Config(os.path.join(os.path.dirname(os.path.dirname(__file__)), "config.yaml"))

if __name__ == "__main__":
    print(Config(path="../config.yaml").config)
