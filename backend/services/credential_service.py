from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import user_crud
from crud import credential_crud

import schemas

class CredentialService:
    """
    Service responsável pelas regras de negócio relacionadas às credenciais.
    """

    def create_credential(
        self,
        db: Session,
        credential: schemas.CredentialCreate,
    ):
        """
        Regra para criação de credenciais.
        """

        # Verifica se já existe uma credencial com o mesmo UID
        if credential_crud.credential_exists(db, credential.uid):
            raise HTTPException(
                status_code=400,
                detail="Já existe uma credencial com o UID informado."
            )
        
        user = user_crud.get_user_by_id(
            db=db, 
            user_id = credential.user_id,
        )
        
        if  user is None:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado."
            )

        return credential_crud.create_credential(
            db=db,
            user_id=credential.user_id,
            uid=credential.uid,
            tipo_credencial=credential.tipo_credencial,
            descricao=credential.descricao,
        )


    def list_credentials(
        self,
        db: Session,
    ):
        """
        Regra para listagem de credenciais.
        """

        return credential_crud.get_all_credentials(db)
    

    def get_credential_by_id(
        self,
        db: Session,
        credential_id: int,
    ):
        """
        Regra para busca de credenciais pelo ID.
        """

        credentialID = credential_crud.get_credential_by_id(db, credential_id)

        if credentialID is None:
            raise HTTPException(
                status_code=404,
                detail="Credencial não encontrada."
            )

        return credentialID


    def get_credential(
        self,
        db: Session,
        uid: str,
    ):
        """
        Regra para busca de credenciais.
        """

        credential = credential_crud.get_credential_by_uid(db, uid)

        if credential is None:
            raise HTTPException(
                status_code=404,
                detail="Credencial não encontrada."
            )

        return credential
    