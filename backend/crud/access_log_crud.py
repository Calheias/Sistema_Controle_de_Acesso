from sqlalchemy.orm import Session

from dto.authentication_result import AuthenticationResult

from models import AccessLog, Credential

import schemas

from enums import CredentialType


def create_access_log(
        db: Session, 
        result: AuthenticationResult,
) -> AccessLog:
    """
    Registra uma tentativa de autenticação.
    """

    access_log: AccessLog = AccessLog(
        credential_id=result.credential_id,
        device_id=result.device_id,
        door_id=result.door_id,
        uid_lido=result.uid,
        resultado=result.autorizado,
        motivo=result.motivo,
    )

    db.add(access_log)
    db.commit()
    db.refresh(access_log)

    return access_log


def get_access_log_by_id(
    db: Session,
    access_log_id: int, 
):
    """
    Busca um registro pelo ID.
    """

    return (
        db.query(AccessLog)
        .filter(AccessLog.id == access_log_id)
        .first()
    )


def get_all_access_logs(
    db: Session,
):
    """
    Retorna todo o histórico.
    """

    return (
        db.query(AccessLog)
        .all()
    )


def get_logs_by_user(
    db: Session,
    user_id: int,
):
    """
    Retorna o histórico de um usuário.
    """ 

    return (
        db.query(AccessLog)
        .join(Credential)
        .filter(Credential.user_id == user_id)
        .all()
    )


def get_logs_by_door(
    db: Session,        
    door_id: int,
):
    """
    Retorna o histórico de uma porta.
    """

    return (  
        db.query(AccessLog)
        .filter(AccessLog.door_id == door_id)
        .all()
    )


def get_logs_by_device(
    db: Session,        
    device_id: int,
):
    """
    Retorna o histórico de uma porta.
    """

    return (  
        db.query(AccessLog)
        .filter(AccessLog.device_id == device_id)
        .all()
    )


def get_logs_by_uid(
    db: Session,
    uid_lido: str,
):
    """
    Retorna o histórico de um UID
    """

    return (
        db.query(AccessLog)
        .filter(AccessLog.uid_lido == uid_lido)
        .all()
    )


def get_logs_by_credential_type(
    db: Session,
    tipo: CredentialType,
):
    """
    Retorna o histórico por tipo de credencial
    """

    return (
        db.query(AccessLog)
        .join(Credential)
        .filter(Credential.tipo_credencial == tipo)
        .all()
    )

