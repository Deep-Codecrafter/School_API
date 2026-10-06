from pydantic import BaseModel ,ConfigDict


class User(BaseModel):
    idd:str
    Password:str

