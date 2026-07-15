from enums import AccessReason


class AuthenticationError(Exception):
    """
    Exceção base para erros de autenticação.
    """
    
    def __init__(self, motivo: AccessReason):
        self.motivo = motivo
        super().__init__(motivo.value)


# Credential Errors
class CredentialNotFound(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.UID_DESCONHECIDO)


class CredentialInactive(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.CREDENCIAL_INATIVA)


class CredentialTypeMismatch(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.TIPO_CREDENCIAL_INVALIDO)


# User Errors
class UserInactive(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.USUARIO_INATIVO)


class UserNotFound(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.USUARIO_DESCONHECIDO)


# Device Errors
class DeviceInactive(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.DISPOSITIVO_INATIVO)


class DeviceNotFound(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.DISPOSITIVO_DESCONHECIDO)


# Door Errors
class DoorInactive(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.PORTA_INATIVA)


class DoorNotFound(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.PORTA_DESCONHECIDA)


#  Door Device
class DoorDeviceMismatch(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.PORTA_NAO_PERTENCE_AO_DISPOSITIVO)


# Permission Errors
class PermissionDenied(AuthenticationError):
    def __init__(self):
        super().__init__(AccessReason.SEM_PERMISSAO)


