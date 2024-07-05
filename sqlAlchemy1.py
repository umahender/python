from sqlalchamy import create_engine,Integer,Column,String
from sqlalchemy.orm import declarative_base
from sqlalchemy.ext.declarative import declarative_base
ba=declarative_base()

class Bank(b):
    __tablename__="Account"
    name=