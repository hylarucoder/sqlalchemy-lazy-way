from sqlalchemy import Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship, Session

from sqlalchemy_lazy_way.smart_query import SmartQuery

engine = create_engine("sqlite://")
session = Session(engine, query_cls=SmartQuery)


class Base(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


class Blog(Base):
    name = Column(String)
    entries = relationship("Entry", backref="blog")


class Entry(Base):
    blog_id = Column(Integer, ForeignKey("blog.id"))
    pub_date = Column(Date)
    headline = Column(String)
    body = Column(String)


Base.metadata.create_all(engine)
