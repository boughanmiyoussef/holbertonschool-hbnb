#!/usr/bin/python3
from datetime import datetime
import uuid

class City:
    def __init__(self, name, country):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.name = name
        self.country = country