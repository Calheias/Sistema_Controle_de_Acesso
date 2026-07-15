"""
Configuração e conexão com o banco de dados.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL


# ======================================================
# Base para todos os modelos do banco
# ======================================================

class Base(DeclarativeBase):
    pass


# ======================================================
# Engine
# ======================================================

engine = create_engine(
    DATABASE_URL,
    echo=True
)


# ======================================================
# Sessões do banco
# ======================================================

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# ======================================================
# Criação das tabelas
# ======================================================

def create_database():
    """
    Cria todas as tabelas definidas nos Models.
    """
    Base.metadata.create_all(bind=engine)


def get_db():
    """
    Fornece uma sessão do banco para cada requisição.
    """

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


"""
# ======================================================
# Testar a conexão com o banco de dados
# ======================================================

1)

Para testar a conexão com o banco de dados, entre na subpasta backend do projeto no terminal com:
'cd backend'

E, ative o 'compilardor' python:
'python'

Depois importe a engine do arquivo database.py:
'from database import engine'

Por fim, printe a engine:
'print(engine)'

Deve aparecer a mensagem 
'Engine(sqlite:///rfid_access.db)' -> Tudo certo!

Saia do 'compilador' python:
'exit()'
"""

"""
2)

Outra forma é utilizando o condicional de ativação do script aqui mesmo, no final do script:

if __name__ == "__main__":
    print(engine)
   
Depois execute no terminal:
'python database.py'  (Botão Run do VSCode)

Se a mensagem 'Engine(sqlite:///rfid_access.db)' aparecer, tudo certo!
"""