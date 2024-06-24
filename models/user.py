#!/user/bin/python3

import uuid
from .base import BaseModel

class User(BaseModel):
    emails_in_database = set()

    def __init__(self, email, password):
        super().__init__()
        if email in User.emails_in_database:
            raise ValueError ("Email Taken")
        User.emails_in_database.add(email)
        self.email = email
        self.password = password
        self.id = str(uuid.uuid4())
