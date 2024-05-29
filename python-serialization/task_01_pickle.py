#!/usr/bin/python3

import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        print out the objs attributes in the specified format.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        serialize the current instance of the object and save it to the provided filename
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing: {e}")
    
    @classmethod
    def deserialize(cls, filename):
        """
        load and return an instance of CustomObject from the provided filename
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
                return obj
        except (FileNotFoundError, pickle.UnpicklingError) as e:
            print(f"An error occurred while deserializing: {e}")
            return None
