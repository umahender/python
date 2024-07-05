from sqlalchamy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
class Abc(Base):
    __tablename__="xyz"
    Id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)

eng=create_engine("sqlite:///mydb.db")
Base.metadata.create_all(eng)
session=sessionmaker(bind=eng)
s=session()
#p=Abc(name="suresh ",age=35)
#s.add(p)
#p1=Abc(name="uma",age=76)
#s.add(p1)
up=s.query(Abc).filter(Abc.name=="mahender").first()
up.age=78
s.commit()
data=s.query(Abc).all()
for x in data:
    print(x.name,x.age)
