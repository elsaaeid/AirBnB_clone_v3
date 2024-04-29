#!/usr/bin/python3
import uuid
from datetime import datetime
from hashlib import md5
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

if models.storage_type == "db":
    Base = declarative_base()
else:
    Base = object


class BaseModel(Base):
    """Base model that all classes will inherit from"""
    __abstract__ = True

    id = Column(String(60), primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)
    password = Column(String(128))

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
        if 'password' in kwargs:
            self.password = md5(kwargs['password'].encode()).hexdigest()

    def __str__(self):
        """Returns the string representation of the instance"""
        cls = type(self).__name__
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, secure_pwd=True):
        """Converts instance into dict format"""
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        if "updated_at" in new_dict:
            new_dict["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        new_dict["__class__"] = type(self).__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        if secure_pwd and models.storage_type == "db":
            del new_dict['password']
        return new_dict

    def delete(self):
        """Delete the current instance from the storage"""
        models.storage.delete(self)
