from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import(
    user_crud,
    door_crud,
    permission_crud,
)

import schemas


class PermissionService:
    """
    Service responsável pelas regras de negócio relacionadas às permissões.
    """

    def create_permission(
        self,
        db: Session,
        permission: schemas.PermissionCreate,
    ):  
        """
        Regra para a criação de permissões
        """
        # Verifica se o usuário existe
        if user_crud.get_user_by_id(db, permission.user_id) is None:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado."
            )
        
        # Verifica se a porta existe
        if door_crud.get_door_by_id(db, permission.door_id) is None:
            raise HTTPException(
                status_code=404, 
                detail="Porta não encontrada."
            )
        
        # Verifica se a permissão já existe
        if permission_crud.permission_exists(
            db, 
            permission.user_id,
            permission.door_id,
        ):
            raise HTTPException(
                status_code=400,
                detail="O usuário já possui permissão para essa porta."
            )
        
        return permission_crud.create_permission(
            db=db,
            user_id=permission.user_id,
            door_id=permission.door_id,
        )
    

    def list_permissions(
        self,
        db: Session,
    ):
        """
        Lista todas as permissões cadastradas.
        """

        return permission_crud.get_all_permissions(db)
    

    def get_permission(
        self,
        db:Session,
        permission_id: int,
    ):
        """
        Busca a permissão pelo ID.
        """

        permission = permission_crud.get_permission_by_id(
            db,
            permission_id,
        )

        if permission is None:
            raise HTTPException(
                status_code=404,
                detail="Permissão não encontrada."
            )
        
        return permission
    

    def list_permissions_by_user(
        self,
        db: Session,
        user_id: int,
    ):
        """
        Lista todas as permissões ativas de um usuário
        """

        if user_crud.get_user_by_id(db, user_id) is None:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado."
            )
        
        return permission_crud.get_permissions_by_user(
            db,
            user_id,
        )


    def list_permissions_by_door(
        self,
        db: Session,
        door_id: int,
    ):
        """
        Lista todas as permissões ativas de uma porta
        """

        if door_crud.get_door_by_id(db, door_id) is None:
            raise HTTPException(
                status_code=404,
                detail="Porta não encontrada."
            )
        
        return permission_crud.get_permissions_by_door(
            db,
            door_id,
        )
    
