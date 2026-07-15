from fastapi import HTTPException
from sqlalchemy.orm import Session

from crud import device_crud
from crud import door_crud

import schemas

class DoorService:
    """
    Service responsável pelas regras de negócio relacionados às portas.
    """
    
    def create_door(
        self,
        db: Session,
        door: schemas.DoorCreate,
    ): 
        """
        Regra para criação de portas.
        """

        # Verifica se já existe uma porta com o mesmo nome
        if door_crud.door_exists(db, door.device_id, door.nome):
            raise HTTPException(
                status_code=400,
                detail="O dispositivo já controla uma porta com este nome."
            )
        
        device = device_crud.get_device_by_id(
            db=db, 
            device_id = door.device_id
        )

        if device is None:
            raise HTTPException(
                status_code=404,
                detail="Dispositivo não encontrado."
        )
        
        return door_crud.create_door(
            db=db,
            device_id=door.device_id,
            nome=door.nome,
        )


    def list_doors(
        self,
        db: Session,
    ):
        """
        Regra para listagem de portas.
        """

        return door_crud.get_all_doors(db)
    

    def search_doors_by_name(
        self,
        db: Session,
        nome: str,
    ):
        """
        Busca portas por parte do nome, 
        não gera erro se não encontrar nada, apenas devolve uma lista vazia.
        """

        portas = door_crud.search_doors_by_name(
            db,
            nome,
        )

        return portas
    
    
    def get_door(
        self,
        db: Session,
        door_id: int,
    ):
        """
        Regra para busca de portas.
        """

        door = door_crud.get_door_by_id(db, door_id)

        if door is None:
            raise HTTPException(
                status_code=404,
                detail="Porta não encontrada."
            )

        return door
    