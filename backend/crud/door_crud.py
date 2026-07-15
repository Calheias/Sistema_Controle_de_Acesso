from sqlalchemy.orm import Session

from models import Door


def create_door(
    db: Session,
    device_id: int,
    nome: str, 
): 
    """
    Cadastra uma nova porta
    """

    door = Door(
        device_id=device_id,
        nome=nome,
        ativo=True,
    )   

    db.add(door)
    db.commit()
    db.refresh(door)

    return door


def get_door_by_id(
        db: Session, 
        door_id: int,
):
    """
    Busca uma porta pelo ID.
    """

    return (
        db.query(Door)
        .filter(Door.id == door_id)
        .first()
    )


def search_doors_by_name(
    db: Session,
    nome: str,
):
    """
    Busca portas pelo nome, 
    o método ilike permite que, com partes do nome, seja possível encontrar todos os registros de nomes completos,
    então Ent, permite encontrar Entrada, Entrada Reserva e etc.
    """

    return (
        db.query(Door)
        .filter(Door.nome.ilike(f"%{nome}%"))
        .all()
    )


def get_all_doors(
    db: Session,
):
    """
    Retorna todos as portas cadastradas.
    """

    return db.query(Door).all()


def door_exists(
    db: Session,
    device_id: int,
    nome: str,
):

    return (
        db.query(Door)
        .filter(Door.device_id == device_id)
        .filter(Door.nome == nome)
        .first()
        is not None
    )

"""
Para concatenar filtros, pode-se fazer de duas formas:

1) Adicionando mais .filter(s) ao return (como acima)

2) Operador Lógico &

.filter(
    (Door.device_id == device_id) &
    (Door.nome == nome)
)
"""