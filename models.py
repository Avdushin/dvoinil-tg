from sqlalchemy import Column, Integer, String, Float, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    category = Column(String(255))
    price = Column(Float)
    description = Column(String(512))

# Создаем таблицу в базе данных
engine = create_engine('sqlite:///products.db')
Base.metadata.create_all(engine)