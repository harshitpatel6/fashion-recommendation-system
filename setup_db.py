from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import POSTGRES_URI

engine = create_engine(POSTGRES_URI)
Base = declarative_base()

class FashionItem(Base):
    __tablename__ = "fashion_items"
    id = Column(Integer, primary_key=True)
    image_url = Column(String, nullable=False)
    style_category = Column(String, nullable=False)
    description = Column(String, nullable=False)

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
