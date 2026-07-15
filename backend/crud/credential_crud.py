from sqlalchemy.orm import Session

from models import Credential

from enums import CredentialType


def create_credential(
    db: Session,
    user_id: int,
    uid: str,
    tipo_credencial: CredentialType,
    descricao: str | None,
):
    """
    Cria uma nova credencial.
    """

    nova_credencial = Credential(
        user_id=user_id,
        uid=uid,
        tipo_credencial=tipo_credencial,
        descricao=descricao,
        ativo=True,
    )

    db.add(nova_credencial)
    db.commit()
    db.refresh(nova_credencial)

    return nova_credencial


def get_credential_by_id(
    db: Session,
    credential_id: int,
):
    """
    Busca uma credencial pelo ID.
    """

    return (
        db.query(Credential)
        .filter(Credential.id == credential_id)
        .first()
    )


def get_credential_by_uid(
    db: Session,
    uid: str,
):
    """
    Busca uma credencial pelo UID.
    """

    return (
        db.query(Credential)
        .filter(Credential.uid == uid)
        .first()
    )
 

def credential_exists(
    db: Session,
    uid: str,
):
    """
    Verifica se já existe uma credencial com o UID informado.
    """

    return (
        db.query(Credential)
        .filter(Credential.uid == uid)
        .first()
        is not None
    )


def get_all_credentials(
    db: Session,
):
    """
    Retorna todas as credenciais cadastradas.
    """

    return db.query(Credential).all()