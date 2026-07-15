from fastapi import Depends
from fastapi import FastAPI
from sqlalchemy.orm import Session

import schemas

from database import create_database
from database import get_db

from services.user_service import UserService
from services.credential_service import CredentialService
from services.device_service import DeviceService
from services.door_service import DoorService
from services.permission_service import PermissionService
from services.access_log_service import AccessLogService
from services.authentication_service import AuthenticationService

from enums import CredentialType

from dto.authentication_result import AuthenticationResult


# Criação do banco de dados
create_database()

# Inicialização do service
user_service = UserService()
credential_service = CredentialService()
device_service = DeviceService()
door_service = DoorService()
permission_service = PermissionService()
access_log_service = AccessLogService()
authentication_service = AuthenticationService()


# Endpoints
app = FastAPI(title="RFID Access Control")

@app.get("/")
def home():
    return {"status": "Sistema iniciado com sucesso!"}

# ============================================
# De usuário
# ============================================
@app.post("/users", response_model=schemas.UserResponse)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):

    return user_service.create_user(
        db,
        user,
    )


@app.get("/users", response_model=list[schemas.UserResponse])
def list_users(
    db: Session = Depends(get_db),
):

    return user_service.list_users(db)


@app.get("/users/search", response_model=list[schemas.UserResponse])
def search_users_by_name(
    nome: str,
    db: Session = Depends(get_db),
):

    return user_service.search_users_by_name(
        db,
        nome,)


@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):

    return user_service.get_user(
        db,
        user_id,
    )


# ============================================
# De credencial
# ============================================
@app.post("/credentials", response_model=schemas.CredentialResponse)
def create_credential(
    credential: schemas.CredentialCreate,
    db: Session = Depends(get_db),
):

    return credential_service.create_credential(
        db,
        credential,
    )


@app.get("/credentials", response_model=list[schemas.CredentialResponse])
def list_credentials(
    db: Session = Depends(get_db),
):

    return credential_service.list_credentials(db)


@app.get("/credentials/{credential_id}", response_model=schemas.CredentialResponse)
def get_credential_by_id(
    credential_id: int,
    db: Session = Depends(get_db),
):

    return credential_service.get_credential_by_id(
        db,
        credential_id,
    )


@app.get("/credentials/uid/{uid}", response_model=schemas.CredentialResponse)
def get_credential(
    uid: str,
    db: Session = Depends(get_db),
):

    return credential_service.get_credential(
        db,
        uid,
    )


# ============================================
# De dispositivo
# ============================================
@app.post("/devices", response_model=schemas.DeviceResponse)
def create_device(
    device: schemas.DeviceCreate,
    db: Session = Depends(get_db),
):

    return device_service.create_device(
        db,
        device,
    )


@app.get("/devices", response_model=list[schemas.DeviceResponse])
def list_devices(
    db: Session = Depends(get_db),
):

    return device_service.list_devices(db)


@app.get("/devices/search", response_model=list[schemas.DeviceResponse])
def search_devices_by_name(
    nome: str,
    db: Session = Depends(get_db),
):

    return device_service.search_devices_by_name(
        db,
        nome,)


@app.get("/devices/{device_id}", response_model=schemas.DeviceResponse)
def get_device(
    device_id: int,
    db: Session = Depends(get_db),
):

    return device_service.get_device(
        db,
        device_id,
    )


@app.get("/devices/ip/{ip}", response_model=schemas.DeviceResponse)
def get_device_by_ip(
    ip: str,
    db: Session = Depends(get_db),
):

    return device_service.get_device_by_ip(
        db,
        ip,
    )


# ============================================
# De porta
# ============================================
@app.post("/doors", response_model=schemas.DoorResponse)
def create_door(
    door: schemas.DoorCreate,
    db: Session = Depends(get_db),
):

    return door_service.create_door(
        db,
        door,
    )


@app.get("/doors", response_model=list[schemas.DoorResponse])
def list_doors(
    db: Session = Depends(get_db),
):

    return door_service.list_doors(db)


@app.get("/doors/{door_id}", response_model=schemas.DoorResponse)
def get_door(
    door_id: int,
    db: Session = Depends(get_db),
):

    return door_service.get_door(
        db,
        door_id,
    )


@app.get("/door/search", response_model=list[schemas.DoorResponse])
def search_doors_by_name(
    nome: str,
    db: Session = Depends(get_db),
):

    return door_service.search_doors_by_name(
        db,
        nome,
    )


# ============================================
# De permissão
# ============================================
@app.post("/permissions", response_model=schemas.PermissionResponse)
def create_permission(
    permission: schemas.PermissionCreate,
    db: Session = Depends(get_db),
):

    return permission_service.create_permission(
        db,
        permission,
    )


@app.get("/permissions", response_model=list[schemas.PermissionResponse])
def list_permissions(
    db: Session = Depends(get_db),
):

    return permission_service.list_permissions(db)


@app.get("/permissions/{permission_id}", response_model=schemas.PermissionResponse)
def get_permission(
    permission_id: int,
    db: Session = Depends(get_db),
):

    return permission_service.get_permission(
        db,
        permission_id,
    )


@app.get("/users/{user_id}/permissions", response_model=list[schemas.PermissionResponse])
def list_permissions_by_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    
    return permission_service.list_permissions_by_user(
        db,
        user_id)


@app.get("/doors/{door_id}/permissions", response_model=list[schemas.PermissionResponse])
def list_permissions_by_door(
    door_id: int,
    db: Session = Depends(get_db),
):
    
    return permission_service.list_permissions_by_door(
        db,
        door_id,
    )


# ============================================
# De auditoria
# ============================================
@app.get("/access-logs", response_model=list[schemas.AccessLogResponse])
def list_access_logs(
    db: Session = Depends(get_db),
):

    return access_log_service.list_access_logs(db)


@app.get("/access-logs/{access_log_id}", response_model=schemas.AccessLogResponse)
def get_access_log(
    access_log_id: int,
    db: Session = Depends(get_db),
):

    return access_log_service.get_access_log(
        db,
        access_log_id,
    )


@app.get("/users/{user_id}/access-logs", response_model=list[schemas.AccessLogResponse])
def list_access_logs_by_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    
    return access_log_service.list_access_logs_by_user(
        db,
        user_id,
    )


@app.get("/doors/{door_id}/access-logs", response_model=list[schemas.AccessLogResponse])
def list_access_logs_by_door(
    door_id: int,
    db: Session = Depends(get_db),
):
    
    return access_log_service.list_access_logs_by_door(
        db,
        door_id,
    )


@app.get("/devices/{device_id}/access-logs", response_model=list[schemas.AccessLogResponse])
def list_access_logs_by_device(
    device_id: int,
    db: Session = Depends(get_db),
):
    
    return access_log_service.list_access_logs_by_device(
        db,
        device_id,
    )


@app.get("/access-logs/uid/{uid}", response_model=list[schemas.AccessLogResponse])
def list_access_logs_by_uid(
    uid: str,
    db: Session = Depends(get_db),
):
    
    return access_log_service.list_access_logs_by_uid(
        db,
        uid,
    )


@app.get("/access-logs/credential-type/{credential_type}", response_model=list[schemas.AccessLogResponse])
def list_access_logs_by_credential_type(
    credential_type: CredentialType,
    db: Session = Depends(get_db),
):
    
    return access_log_service.list_access_logs_by_credential_type(
        db,
        credential_type,
    )


# ============================================
# De autenticação
# ============================================
@app.post("/authenticate", response_model=AuthenticationResult)
def authenticate(
    request: schemas.AuthenticateRequest,
    db: Session = Depends(get_db),
):

    return authentication_service.authenticate(
        db,
        request,
    )