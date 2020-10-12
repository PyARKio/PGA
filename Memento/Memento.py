# -- coding: utf-8 --
from __future__ import unicode_literals
from Arsenal.Chronicler import log
import pymongo
import bson
import abc
# import config


__author__ = 'PyARK'
__version__ = "1.0.1"
__email__ = "fedoretss@gmail.com"
__status__ = "Production"


class MetaMongodbHandler(abc.ABCMeta):
    def __new__(mcs, name, bases, attrs):
        cls = super().__new__(mcs, name, bases, attrs)
        if bases:
            database_name = attrs.get('database_name', getattr(cls, 'database_name', None))
            assert isinstance(database_name, str), \
                'You have to set `database_name` attribute (string) to `{}` class'.format(name)
            collection_name = attrs.get('collection_name', getattr(cls, 'collection_name', None))
            assert isinstance(collection_name, str), \
                'You have to set `collection_name` attribute (string) in `{}` class'.format(name)
            _client = getattr(cls, '_client', None)
            assert isinstance(_client, pymongo.MongoClient), \
                'You have to set `_client` attribute (pymongo MongoClient) to `{}` class'.format(name)
        return cls

    @property
    def database(cls):
        if not hasattr(cls, '_database'):
            cls._database = cls._client[cls.database_name]
        return cls._database

    @property
    def collection(cls):
        if not hasattr(cls, '_collection'):
            cls._collection = cls.database[cls.collection_name]
        return cls._collection


class BaseMongodbHandler(metaclass=MetaMongodbHandler):
    _client = pymongo.MongoClient()
    database_name = 'Currency'

    @staticmethod
    @abc.abstractmethod
    def collection_name():  # pragma: no cover
        pass

    @staticmethod
    @abc.abstractmethod
    def db_fields():  # pragma: no cover
        pass

    @classmethod
    def validate_incoming_data(cls, data):
        return {key: value for key, value in data.items() if key in cls.db_fields}

    @classmethod
    def get_all_objects(cls, projection=None):
        return list(cls.collection.find({}, projection=projection))

    @classmethod
    def get_one_obj(cls, filter, projection=None):
        return cls.collection.find_one(filter, projection=projection)

    @classmethod
    def insert_obj(cls, data):
        log.debug('\n\n\n')
        log.debug(cls.collection_name)
        log.debug(data)

        data = cls.validate_incoming_data(data)
        result = cls.collection.insert_one(data)
        data['_id'] = result.inserted_id
        return data

    @classmethod
    def update_obj_by_id(cls, _id, data, upsert=False):
        if not isinstance(_id, bson.ObjectId):
            _id = bson.ObjectId(_id)
        data = cls.validate_incoming_data(data)
        if data:
            return cls.collection.update_one({'_id': _id}, {'$set': data}, upsert=upsert)

    @classmethod
    def delete_obj_by_id(cls, _id):
        if not isinstance(_id, bson.ObjectId):
            _id = bson.ObjectId(_id)
        return cls.collection.delete_one({'_id': _id})

    @classmethod
    def delete_all_obj(cls):
        return cls.collection.delete_many({})







