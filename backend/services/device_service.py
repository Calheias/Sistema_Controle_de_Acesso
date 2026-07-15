from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import device_crud

import schemas

class DeviceService:
    """
    Service responsável pelas regras de negócio relacionados aos dispositivos.
    """

    def create_device(
        self,
        db: Session,
        device: schemas.DeviceCreate,
    ):  
        """
        Regra para o cadastro de dispositivos.
        """
        
        # Verifica se já existe um dispositivo com o mesmo IP
        if device_crud.device_exists(db, device.ip):
            raise HTTPException(
                status_code=400,
                detail="Já existe um dispositivo com o IP informado."
            )
        
        return device_crud.create_device(
            db=db,
            ip=device.ip,
            nome=device.nome,
            localizacao=device.localizacao,
        )
    

    def list_devices(
        self,
        db: Session,
    ):
        """
        Listagem de dispositivos.
        """

        return device_crud.get_all_devices(db)
    

    def search_devices_by_name(
        self,
        db: Session,
        nome: str,
    ):
        """
        Busca usuários por parte do nome, 
        não gera erro se não encontrar nada, apenas devolve uma lista vazia.
        """

        dispositivos = device_crud.search_devices_by_name(
            db,
            nome,
        )

        return dispositivos
    

    def get_device(
        self,
        db: Session,
        device_id: int,
    ):
        """
        Busca um dispositivo pelo ID.
        """

        device = device_crud.get_device_by_id(
            db=db, 
            device_id=device_id,
        )

        if device is None:
            raise HTTPException(
                status_code=404,
                detail="Dispositivo não encontrado."
            )

        return device
    

    def get_device_by_ip(
        self,
        db: Session,
        ip: str,
    ):
        """
        Busca um dispositivo pelo IP.
        """

        deviceIP = device_crud.get_device_by_ip(
            db, 
            ip,
        )

        if deviceIP is None:
            raise HTTPException(
                status_code=404,
                detail="Dispositivo não encontrado."
            )

        return deviceIP