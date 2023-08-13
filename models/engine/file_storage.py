#!/usr/bin/python3
"""The file storage module"""
import json
from models.base_model import BaseModel


class FileStorage:
    """class storage that serializes instances
    to a JSON file and deserializes JSON to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the __objects dict"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key
        <obj class name>.id"""
        key = "{0}.{1}".format(type(obj.__name__, obj.id)
        self.__objects[key]=obj

    def save(self):
        """serilizes the __objects to a JSON file(path:__file_path"""
        s_obj={}
        for key, obj in self.__objects.items():
            s_obj[key]=obj.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(s_obj, f)

    def reload(self):
        """deserializes the json file to __objects(only if JSON file
        (file__path)exists;otherwise,do nothing.If the file doesn't
        exist,no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                ds_obj=json.load(f)
                for key, value in ds_obj.items():
                    class_name=key.split('.')[0]
                    cls=eval(class_name)
                    self.__objects[key]=cls(**value)
        except FileNotFoundError:
            pass
