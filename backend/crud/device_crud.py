from sqlalchemy.orm import Session

from models import Device


def create_device(
    db: Session,
    ip: str,
    nome: str,
    localizacao: str,
): 
    """
    Cadastra um novo dispositivo
    """

    device = Device(
        ip=ip,
        nome=nome,
        localizacao=localizacao,
        ativo=True,
    )

    db.add(device)
    db.commit()
    db.refresh(device)

    return device


def get_device_by_id(
    db: Session,
    device_id: int,
):
    """
    Busca um dispositivo pelo ID.
    """

    return (
        db.query(Device)
        .filter(Device.id == device_id)
        .first()
    )


def get_device_by_ip(
    db: Session,
    ip: str,
):
    """
    Busca um dispositivo pelo IP.
    """

    return (
        db.query(Device)
        .filter(Device.ip == ip)
        .first()
    )


def search_devices_by_name(
    db: Session,
    nome: str,
):
    """
    Busca dispositivos pelo nome, 
    o método ilike permite que, com partes do nome, seja possível encontrar todos os registros de nomes completos,
    então ES, permite encontrar ESP32, ESP8266 e etc.
    """

    return (
        db.query(Device)
        .filter(Device.nome.ilike(f"%{nome}%"))
        .all()
    )


def get_all_devices(
    db: Session,
):
    """
    Retorna todos os dispositivos cadastrados.
    """

    return db.query(Device).all()


def device_exists(
    db: Session,
    ip: str,
):
    """
    Verifica se já existe um dispositvo com o IP informado.
    """

    return (
        db.query(Device)
        .filter(Device.ip == ip)
        .first()
        is not None
    )
