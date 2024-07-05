#The declarative_base combines a metadata container and a mapper that maps our class to a database table.
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class Employee(Base):
    __tablename__="emp"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    rno=Column(Integer)
    section=Column(String)
engine=create_engine('sqlite:///empdata.db')
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
