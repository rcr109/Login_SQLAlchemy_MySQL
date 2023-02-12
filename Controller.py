import hashlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Model import Pessoa


def return_session():
    host = "localhost"
    db = "login_alchemy"
    user = "root"
    password = "Mysql202300!"
    port = 3306
    connection = f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    engine = create_engine(connection, echo=False)
    Session = sessionmaker(bind=engine)
    return Session()    

class ControllerCadastro():
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200 or len(email) < 8:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        return 1
  
    @classmethod        
    def cadastrar(cls, nome, email, senha):
        session = return_session()
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all()
        if len(usuario) > 0:
            return 5
        dados_verificados = cls.verifica_dados(nome, email, senha)
        if dados_verificados != 1:
            return dados_verificados
        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            pessoa = Pessoa(nome=nome, email=email, senha=senha)
            session.add(pessoa)
            session.commit()
            return 1
        except:
            return 6
        

class ControllerLogin:
    @classmethod
    def login(cls, email, senha):
        session = return_session()
        senha_encod = hashlib.sha256(senha.encode()).hexdigest()
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha_encod).all()
        if len(logado) == 1:
            return {'logado' : True, 'id' : logado[0].id}
        return False
    

#print(ControllerCadastro.cadastrar('ricardo', 'rcr109@hotmail.com', '1234568910'))

#print(ControllerLogin.login('rcr109@hotmail.com', '1234568910'))
