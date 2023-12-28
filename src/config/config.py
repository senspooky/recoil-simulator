import tomllib
from typing import Dict, Any

class Configuration():
    def __init__(self, path = "config.toml"):
        self.__path = path
        self.__config:Dict[str, Any] = dict()
        
    def load(self):
        with open(self.__path, "rb") as f:
            self.__config = tomllib.load(f)
        
    def get(self, key:str) -> Any:
        return self.__config[key] if self.__config[key] else dict()