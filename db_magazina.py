from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship,scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///blog.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Kategor(Base):
    __tablename__ = 'kategorii'
    id = Column(Integer, primary_key=True)
    kategory_name = Column(String(75))
    kategory_info = Column(String(70))
    kategory_image = Column(String(120))
    posts = relationship('Tovar', backref='author')

    def __init__(self, kategory_name=None, kategory_info=None, kategory_image=None):
        self.kategory_name = kategory_name
        self.kategory_info = kategory_info
        self.kategory_image = kategory_image

    def __repr__(self):
        return '<Kategor {} {}>'.format(self.kategory_name, self.kategory_info)

class Tovar(Base):
    __tablename__ = 'tovari'
    id = Column(Integer, primary_key=True)
    tovar_name = Column(String(75))
    tovar_info = Column(String(70))
    tovar_image = Column(String(120))
    tovar_made = Column(String(70))
    tovar_price = Column(Integer(70))
    kategory_id = Column(Integer, ForeignKey('kategorii.id'))

    def __init__(self, tovar_name=None, tovar_info=None, tovar_image=None,tovar_made=None,tovar_price=None):
        self.tovar_name = tovar_name
        self.tovar_info = tovar_info
        self.tovar_image = tovar_image
        self.tovar_made = tovar_made
        self.tovar_price = tovar_price

    def __repr__(self):
        return '<Tovar {} {}>'.format(self.tovar_name, self.tovar_info)


if __name__ == "__main__" :
	Base.metadata.create_all(bind=engine)        