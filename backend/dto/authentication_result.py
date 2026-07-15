from pydantic import BaseModel

from enums import AccessReason, CredentialType


class AuthenticationResult(BaseModel):
    """
    Representa o resultado de uma tentativa de autenticação.
    """

    autorizado: bool
    motivo: AccessReason
    credential_id: int | None = None
    credential_type: CredentialType | None = None
    user_id: int | None = None
    device_id: int | None = None
    door_id: int | None = None
    uid: str | None = None

    model_config = {
        "from_atributes": True
    }