"""
Service responsável por autenticar tentativas de acesso.
"""
from sqlalchemy.orm import Session

from exceptions.authentication_exceptions import(
    AuthenticationError,
    CredentialNotFound,
    CredentialInactive,
    CredentialTypeMismatch,
    UserNotFound,
    UserInactive,
    DeviceNotFound,
    DeviceInactive,
    DoorNotFound,
    DoorInactive,
    DoorDeviceMismatch,
    PermissionDenied,
)

from enums import AccessReason

from dto.authentication_result import AuthenticationResult

from crud import (
    access_log_crud,
    credential_crud,
    device_crud,
    door_crud,
    permission_crud,
    user_crud,
)

import schemas 


class AuthenticationService:
    def authenticate(
            self, 
            db: Session, 
            request: schemas.AuthenticateRequest,
        ) -> AuthenticationResult:
        
        try:
            credential = credential_crud.get_credential_by_uid(
                db=db,
                uid=request.uid,
            )

            if credential is None:
                raise CredentialNotFound()
            
            if not credential.ativo:
                raise CredentialInactive()
            
            if credential.tipo_credencial != request.tipo_credencial:
                raise CredentialTypeMismatch()


            user = user_crud.get_user_by_id(
                db=db,
                user_id=credential.user_id,
            )

            if user is None:
                raise UserNotFound()
            
            if not user.ativo:
                raise UserInactive()
            

            device = device_crud.get_device_by_id(
                db=db,
                device_id=request.device_id,
            )

            if device is None:
                raise DeviceNotFound()
            
            if not device.ativo:
                raise DeviceInactive()
            

            door = door_crud.get_door_by_id(
                db=db,
                door_id=request.door_id,
            )

            if door is None:
                raise DoorNotFound()
            
            if not door.ativo:
                raise DoorInactive()
            
            if door.device_id != request.device_id:
                raise DoorDeviceMismatch()
            

            if not permission_crud.has_permission(
                db=db,
                user_id=user.id,
                door_id=door.id,
            ):
                raise PermissionDenied()


            # Aqui faz sentido manter os objetos *., pq os dados passaram por uma série de validações (acima) e foram sucessos.
            resultado = AuthenticationResult(
                autorizado=True,
                motivo=AccessReason.AUTORIZADO, 
                credential_id=credential.id,
                credential_type=credential.tipo_credencial,
                user_id=user.id,
                device_id=device.id,
                door_id=door.id,
                uid=credential.uid,
            )
            
        
        # Já aqui, o caso é de insucesso (dado inválido em algum teste) e a variável nunca virou um objeto válido, 
        # portanto, para identificação do erro e auditoria, mantém-se os dados de entrada (recebidos da API/usuário)  
        except AuthenticationError as error:
            resultado = AuthenticationResult(
                autorizado=False,
                motivo=error.motivo,
                uid=request.uid,
                device_id=request.device_id,
                door_id=request.door_id,
            )

        # Registra toda tentativa de autenticação, autorizada ou negada 
        access_log_crud.create_access_log(
            db=db,
            result=resultado,
        )

        return resultado