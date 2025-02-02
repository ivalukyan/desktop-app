from sqlalchemy import Column, String, BigInteger, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


db_url = "mysql+pymysql://root:root@localhost:3306/my_db"

engine = create_engine(db_url, pool_pre_ping=True, pool_recycle=300)

SessionMaker = sessionmaker(bind=engine)

Base = declarative_base()


class Products(Base):
    __tablename__ = 'products'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    material_name = Column(String(50), nullable=False)
    material_type = Column(String(50), nullable=False)
    material_img = Column(String(50), nullable=True)
    material_price = Column(String(50), nullable=False)
    quantity_in_stoke = Column(String(50), nullable=False)
    min_quantity = Column(Integer, nullable=False)
    quantity_in_box = Column(Integer, nullable=False)
    measurement = Column(String(50), nullable=False)


class Traffic(Base):
    __tablename__ = 'traffic'
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    material_name = Column(String(50), nullable=False)
    possible_delivery = Column(String(100), nullable=False)


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
