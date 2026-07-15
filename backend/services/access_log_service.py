"""
Service responsável pelas consultas ao histórico de acessos.
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import (
    access_log_crud,
    user_crud,   
    door_crud,
    device_crud,
)

from enums import CredentialType


class AccessLogService:
    """
    Consultas ao histórico de acessos
    """
    def list_access_logs(
        self,
        db: Session,
    ):
        """
        Lista todo o histórico de acessos.
        """

        return access_log_crud.get_all_access_logs(db)
    

    def get_access_log(
        self,
        db: Session,
        access_log_id: int,
    ):
        """
        Consulta registro pelo ID
        """

        access_log = access_log_crud.get_access_log_by_id(
            db,
            access_log_id,
        )

        if access_log is None:
            raise HTTPException(
                status_code=404,
                detail="Registro de acesso não encontrado."
            )

        return access_log
    

    def list_access_logs_by_user(
        self,
        db: Session,
        user_id: int
    ):
        """
        Consulta o histórico de um usuário.
        """ 

        if user_crud.get_user_by_id(db, user_id) is None:
            raise HTTPException(
                status_code=404,
                detail="Usuário não encontrado."
            )
        
        return access_log_crud.get_logs_by_user(
            db,
            user_id,
        )
    

    def list_access_logs_by_door(
        self,
        db: Session,
        door_id: int,
    ):
        """
        Consulta o histórico de uma porta.
        """ 
        
        if door_crud.get_door_by_id(db, door_id) is None:
            raise HTTPException(
                status_code=404,
                detail="Porta não encontrada."
            )
        
        return access_log_crud.get_logs_by_door(
            db,
            door_id,
        )
    

    def list_access_logs_by_device(
        self,
        db: Session,
        device_id: int,
    ):
        """
        Consulta o histórico de um dispositivo.
        """ 
        
        if device_crud.get_device_by_id(db, device_id) is None:
            raise HTTPException(
                status_code=404,
                detail="Dispositivo não encontrado."
            )
        
        return access_log_crud.get_logs_by_device(
            db,
            device_id,
        )
    

    def list_access_logs_by_uid(
        self,
        db: Session,
        uid_lido: str,
    ):
        """
        Consulta o histórico de acessos por UID.
        """ 
        
        return access_log_crud.get_logs_by_uid(
            db,
            uid_lido,
        )


    def list_access_logs_by_credential_type(
        self,
        db: Session,
        tipo: CredentialType
    ):   
        """
        Consulta o histórico por tipo de credencial.
        """ 
        
        return access_log_crud.get_logs_by_credential_type(
            db,
            tipo,
        )