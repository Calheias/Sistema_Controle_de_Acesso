from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import user_crud
import schemas as user_schemas

class UserService:
    """
    Service responsável pelas regras de negócio relacionadas aos usuários.
    """

    # def __init__(self):
        # pass    

    def create_user(
        self,
        db: Session,
        user: user_schemas.UserCreate,
    ):
        """
        Regra para criação de usuários.
        """

        return user_crud.create_user(
            db=db,
            nome=user.nome
        )
    

    def list_users(
        self,
        db: Session,
    ):
        """
        Lista todos os usuários.
        """

        return user_crud.get_all_users(db)


    def search_users_by_name(
        self,
        db: Session,
        nome: str,
    ):
        """
        Busca usuários por parte do nome, 
        não gera erro se não encontrar nada, apenas devolve uma lista vazia.
        """

        usuarios = user_crud.search_users_by_name(
            db,
            nome,
        )

        return usuarios
    

    def get_user(
        self,
        db: Session,
        user_id: int,
    ):
        """
        Busca um usuário pelo ID.
        """

        usuario = user_crud.get_user_by_id(
            db,
            user_id,
        )

        if usuario is None:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado."
            )

        return usuario
  
"""
As condições de existêcia de UID foi passada para Credential, pois agora a criação de um elemento é feita em 2 etapas, 
com o cadastro da pessoa e depois a criação da credencial. 

Por conta disso a remoção de user_exists do user_crud
"""