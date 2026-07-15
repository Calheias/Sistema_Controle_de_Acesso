from sqlalchemy.orm import Session

from models import Permission


def create_permission(
    db: Session,
    user_id: int,
    door_id: int,
):
    """
    Cria uma nova permissão
    """
    permission = Permission(
        user_id=user_id,
        door_id=door_id,
        ativo=True,
    )   

    db.add(permission)
    db.commit()
    db.refresh(permission)

    return permission


def get_permission_by_id(
    db: Session,
    permission_id: int,
):
    """
    Busca uma permissão pelo ID.
    """

    return (
        db.query(Permission)
        .filter(Permission.id == permission_id)
        .first()
    )


def get_all_permissions(
    db: Session,
):
    """
    Retorna todos as permissões cadastradas.
    """

    return db.query(Permission).all()


def get_permissions_by_user(
    db: Session,
    user_id: int,
):
    """
    Busca todas as permissões ativas de um usuário
    """

    return (
        db.query(Permission)
        .filter(
            Permission.user_id == user_id,
            Permission.ativo.is_(True),
        )
        .all()
    )


def get_all_permissions_by_user(
    db: Session,
    user_id: int,
):   
    """
    Busca todas as permissões de um usuário.

    Dados possivelmente relevantes para administração e análise do sistema.
    """

    return (
        db.query(Permission)
        .filter(Permission.user_id == user_id)
        .all()
    )

    
def get_permissions_by_door(
    db: Session,
    door_id: int,
):
    """
    Busca todas as permissões ativas de uma porta
    """

    return (
        db.query(Permission)
        .filter(
            Permission.door_id == door_id,
            Permission.ativo.is_(True),
        )
        .all()
    )


def get_all_permissions_by_door(
    db: Session,
    door_id: int,
):   
    """
    Busca todas as permissões de uma porta.

    Dados possivelmente relevantes para administração e análise do sistema.
    """

    return (
        db.query(Permission)
        .filter(Permission.door_id == door_id)
        .all()
    )

    
def permission_exists(
    db: Session,
    user_id: int,
    door_id: int,
):
    """
    Verifica se a permissão já foi cadastrada
    """

    return (
        db.query(Permission)
        .filter(Permission.user_id == user_id)
        .filter(Permission.door_id == door_id)
        .first()
        is not None
    )


def has_permission(
    db: Session, 
    user_id: int, 
    door_id: int
) -> bool:
    """
    Verifica se o usuário possui permissão para acessar a porta.
    """

    permission = (
        db.query(Permission)
        .filter(
            Permission.user_id == user_id,
            Permission.door_id == door_id,
            Permission.ativo.is_(True),
            # Permission.ativo == True,  -> mesma coisa que o de cima, mas evita transtorno ao mudar de bd
        )
        .first()
    )

    return permission is not None

"""
Responder a  permissão com um booleano, evita que este módulo precise coletar informações extras de outras tabelas
"""

