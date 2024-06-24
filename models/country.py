#!/usr/bin/python3
import uuid
from .base import BaseModel


class Country(BaseModel):
    def __init__(self, name):
        super().__init__()
        self.id = str(uuid.uuid4())
        self.name = name
