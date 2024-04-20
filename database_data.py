from properties import PROPERTIES
import pymongo


class DATABASE_DATA:
    properties = object()
    client = object()

    def __init__(self):
        self.properties = PROPERTIES()
        self.client = pymongo.MongoClient(self.properties.connection_string_to_database).get_database('MathBoat')
