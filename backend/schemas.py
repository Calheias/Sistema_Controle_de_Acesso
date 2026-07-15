"""
Representação dos dados de entrada e saída da API.  # Pydantic 
"""
from pydantic import BaseModel

from enums import CredentialType, AccessReason

from datetime import datetime


# ============================================
# Usuário
# ============================================
class UserCreate(BaseModel):
    """
    Dados necessários para criar um usuário.
    """

    nome: str


class UserResponse(BaseModel):
    """
    Dados retornados pela API.
    """

    id: int
    nome: str
    ativo: bool

    model_config = {
        "from_attributes": True
    }

# ============================================
# Credencial
# ============================================
class CredentialCreate(BaseModel):
    """
    Dados necessários para criar uma credencial.
    """

    user_id: int
    uid: str
    tipo_credencial: CredentialType
    descricao: str | None = None    


class CredentialResponse(BaseModel):
    """
    Dados retornados pela API.
    """

    id: int
    user_id: int
    uid: str
    tipo_credencial: CredentialType
    descricao: str | None = None
    ativo: bool

    model_config = {
        "from_attributes": True
    }


# ============================================
# Dispositivo
# ============================================
class DeviceCreate(BaseModel):
    """
    Dados de cadastro de um dispositivo.
    """

    ip: str
    nome: str
    localizacao: str


class DeviceResponse(BaseModel):
    """
    Dados de dispositivo retornados pela API
    """

    id: int
    ip: str
    nome: str
    localizacao: str
    ativo: bool

    model_config = {
        "from_attributes": True
    }


# ============================================
# Porta
# ============================================
class DoorCreate(BaseModel):
    """
    Dados de cadastro de uma porta.
    """

    device_id: int
    nome: str


class DoorResponse(BaseModel):
    """
    Dados de porta retornados pela API.
    """

    id: int
    device_id: int
    nome: str
    ativo: bool

    model_config = {
        "from_attributes": True
    }    


# ============================================
# Permissão
# ============================================
class PermissionCreate(BaseModel):
    """
    Dados de cadastro de uma permissão.
    """

    user_id: int
    door_id: int


class PermissionResponse(BaseModel):
    """
    Dados de permissão retornados pela API.
    """

    id: int
    user_id: int
    door_id: int
    ativo: bool

    model_config = {
        "from_attributes": True
    }    


# ============================================
# Auditoria - Log de Acesso
# ============================================
class AccessLogResponse(BaseModel):
    """
    Dados de acesso retornados pela API.
    """

    id: int
    credential_id: int | None
    uid_lido: str
    device_id: int
    door_id: int
    resultado: bool
    motivo: AccessReason
    data_hora: datetime 

    model_config = {
        "from_attributes": True
    }    
   

# ============================================
# Autenticação
# ============================================
class AuthenticateRequest(BaseModel):
    """
    Dados necessários para autenticar uma credencial (recebidas do arduino).
    """

    uid: str
    tipo_credencial: CredentialType
    device_id: int
    door_id: int






"""
class AuthenticateResponse(BaseModel):

    Resposta da autenticação (retorna para o arduino).


    autorizado: bool
    motivo: AccessReason 

    
essa classe ficou redundante ao tornar AuthenticateResult em BaseModel
"""