from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = "localhost"
db = "login_alchemy"
user = "root"
password = "Mysql202300!"
port = 3306 #ou a específica do servidor
connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(connection, echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    email = Column(String(200))
    senha = Column(String(100))

Base.metadata.create_all(engine)