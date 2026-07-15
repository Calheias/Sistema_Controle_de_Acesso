from sqlalchemy.orm import Session

from models import User


def create_user(
    db: Session,
    nome: str,
):
    """
    Cria um novo usuário.
    """

    novo_usuario = User(
        nome=nome,
        ativo=True,
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    return novo_usuario


def get_user_by_id(
    db: Session,
    user_id: int,
):
    """
    Busca um usuário pelo ID.
    """

    return (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )


def search_users_by_name(
    db: Session,
    nome: str,
):
    """
    Busca usuários pelo nome, 
    o método ilike permite que, com partes do nome, seja possível encontrar todos os registros de nomes completos,
    então Gab, permite encontrar Gabriel, Gabriela, Gabrielly e etc.
    """

    return (
        db.query(User)
        .filter(User.nome.ilike(f"%{nome}%"))
        .all()
    )


def get_all_users(
    db: Session,
):
    """
    Retorna todos os usuários cadastrados.
    """

    return db.query(User).all()
