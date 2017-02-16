from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship,scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///internet_magaz.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Kategor(Base):
    __tablename__ = 'kategorii'
    id = Column(Integer, primary_key=True)
    kategory_name = Column(String(75))
    kategory_info = Column(String(70))
    kategory_image = Column(String(120))
    kategor = relationship('Tovar', backref='kategorii')

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
    tovar_price = Column(Integer)
    kategory_id = Column(Integer, ForeignKey('kategorii.id'))
    tovars = relationship('Tovar_inphoto', backref='tovari')

    def __init__(self, tovar_name=None, tovar_info=None, tovar_image=None,tovar_made=None,tovar_price=None,kategory_id = None):
        self.tovar_name = tovar_name
        self.tovar_info = tovar_info
        self.tovar_image = tovar_image
        self.tovar_made = tovar_made
        self.tovar_price = tovar_price
        self.kategory_id = kategory_id

    def __repr__(self):
        return '<Tovar {} {}>'.format(self.tovar_name, self.tovar_info)

class Tovar_inphoto(Base):
    __tablename__ = 'tovarinphoto'
    id = Column(Integer, primary_key=True)
    tovarinphoto_info = Column(String(70))
    tovarinphoto_image = Column(String(500))
    tovarinphoto_proizv = Column(String(70))
    tovarinphoto_diagon = Column(String(70))
    tovarinphoto_ram = Column(String(70))
    tovarinphoto_akb = Column(String(70))
    tovarinphoto_osnkamera = Column(String(70))
    tovarinphoto_opsystem = Column(String(70))
    tovarinphoto_color = Column(String(70))
    tovarinphoto_cpu = Column(String(70))
    tovarinphoto_razreshenie = Column(String(70))
    tovarinphoto_frontkamera = Column(String(70))
    tovarinphoto_scaner = Column(String(70))
    tovarinphoto_3g = Column(String(70))
    tovarinphoto_gps = Column(String(70))
    tovarinphoto_matrix = Column(String(70))
    tovar_id = Column(Integer, ForeignKey('tovari.id'))
    tovarim = relationship('Tovar_img', backref='tovarinphoto')

    def __init__(self, tovarinphoto_info=None, tovarinphoto_image=None,  tovarinphoto_proizv=None,tovarinphoto_diagon=None,\
        tovarinphoto_ram=None, tovarinphoto_akb=None,tovarinphoto_osnkamera=None,tovarinphoto_opsystem=None,tovarinphoto_color=None,\
        tovarinphoto_cpu=None,tovarinphoto_razreshenie=None,tovarinphoto_frontkamera=None,tovarinphoto_scaner=None,\
        tovarinphoto_3g=None,tovarinphoto_gps=None,tovarinphoto_matrix=None,tovar_id=None):
       
        self.tovarinphoto_info = tovarinphoto_info
        self.tovarinphoto_image = tovarinphoto_image
        self.tovarinphoto_proizv = tovarinphoto_proizv
        self.tovarinphoto_diagon = tovarinphoto_diagon
        self.tovarinphoto_ram = tovarinphoto_ram
        self.tovarinphoto_akb = tovarinphoto_akb
        self.tovarinphoto_osnkamera = tovarinphoto_osnkamera
        self.tovarinphoto_opsystem = tovarinphoto_opsystem
        self.tovarinphoto_color = tovarinphoto_color
        self.tovarinphoto_cpu = tovarinphoto_cpu
        self.tovarinphoto_razreshenie = tovarinphoto_razreshenie
        self.tovarinphoto_frontkamera = tovarinphoto_frontkamera
        self.tovarinphoto_scaner = tovarinphoto_scaner
        self.tovarinphoto_3g = tovarinphoto_3g
        self.tovarinphoto_gps =tovarinphoto_gps
        self.tovarinphoto_matrix = tovarinphoto_matrix
        self.tovar_id = tovar_id

    def __repr__(self):
        return '<Tovar_inphoto {}>'.format( self.tovarinphoto_info)


class Tovar_img(Base):
    __tablename__ = 'tovarimg'
    id = Column(Integer, primary_key=True)
    tovar_name = Column(String(120))
    tovar_image = Column(String(120))
    tovarinphoto_id = Column(Integer, ForeignKey('tovarinphoto.id'))

    def __init__(self, tovar_name=None,tovar_image=None,kategory_id = None):
        self.tovar_name = tovar_name
        self.tovar_image = tovar_image
        self.tovarinphoto_id = tovarinphoto_id

    def __repr__(self):
        return '<Tovar_img {} {}>'.format(self.tovar_name, self.tovar_info)


class Tovar_photo(Base):
    __tablename__ = 'tovarphoto'
    id = Column(Integer, primary_key=True)
    tovarphoto_info = Column(String(70))
    tovarphoto_image = Column(String(500))
    tovarphoto_id = Column(Integer, ForeignKey('tovari.id'))
    tovarphoto_test = Column(String(70))
    def __init__(self, tovarphoto_info=None, tovarphoto_image=None, tovarphoto_id=None,tovarphoto_test = None,):
       
        self.tovarphoto_info = tovarphoto_info
        self.tovarphoto_image = tovarphoto_image
        self.tovarphoto_id = tovarphoto_id
        self.tovarphoto_test = tovarphoto_test
        

    def __repr__(self):
        return '<Tovar_photo {}>'.format( self.tovarphoto_info)


if __name__ == "__main__" :
	Base.metadata.create_all(bind=engine)        