"""
Representação em Python das tabelas no banco de dados.  # SQLAlchemy ORM
"""

from sqlalchemy import Boolean, DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Enum as SQLEnum
from sqlalchemy import UniqueConstraint

from database import Base
from datetime import datetime, timezone

from enums import CredentialType, AccessReason

class User(Base):
    """
    Representa um usuário no sistema.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    # Entidade-Pai
    credentials: Mapped[list["Credential"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )
    permissions: Mapped[list["Permission"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan"
    )


class Credential(Base):
    """
    Representa as credenciais de acesso.
    """

    __tablename__ = "credentials"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )

    tipo_credencial: Mapped[CredentialType] = mapped_column(
        SQLEnum(CredentialType),
        nullable=False
    )

    uid: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    descricao: Mapped[str] = mapped_column(
        String(100),  # Breve descrição sobre a credencial
        nullable=True
    )

    # Entidade-Pai
    access_logs: Mapped[list["AccessLog"]] = relationship(
        back_populates="credential"
    )
    # Entidade-Filha
    user: Mapped["User"] = relationship(
        back_populates="credentials"
    )


class Device(Base):
    """
    Representa os dispositivos associados ao sistema.
    """

    __tablename__ = "devices"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    ip: Mapped[str] = mapped_column(
        String(45),
        unique=True,
        nullable=False
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    localizacao: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    # Entidade-Pai
    doors: Mapped[list["Door"]] = relationship(
        back_populates="device",
        cascade="all, delete-orphan"
    )
    access_logs: Mapped[list["AccessLog"]] = relationship(
        back_populates="device"
    )


class Door(Base):
    """
    Representa as portas do sistema (se um dispositivo atender a mais de uma porta).
    """

    __tablename__ = "doors"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    device_id: Mapped[int] = mapped_column(
        ForeignKey("devices.id"),
        nullable=False
    )    

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    
    # Entidade-Pai
    permissions: Mapped[list["Permission"]] = relationship(
        back_populates="door",
        cascade="all, delete-orphan"
    )
    access_logs: Mapped[list["AccessLog"]] = relationship(
        back_populates="door"
    )
    # Entidade-Filha
    device: Mapped["Device"] = relationship(
        back_populates="doors"
    )


class Permission(Base):
    """
    Representa as permissões de acesso ao sistema.
    """

    __tablename__ = "permissions"

    __table_args__= (
        UniqueConstraint(
            "user_id",
            "door_id",
            name="uq_permission_user_door",
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
        nullable=False
    )    

    door_id: Mapped[int] = mapped_column(
        ForeignKey("doors.id"),
        nullable=False
    )     

    ativo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    ) 

    # Entidade-Filha
    user: Mapped["User"] = relationship(
        back_populates="permissions"
    )
    door: Mapped["Door"] = relationship(
        back_populates="permissions"
    )


class AccessLog(Base):
    """
    Representa as tentativas de acesso ao sistema válidas ou não.
    """

    __tablename__ = "log_access"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    credential_id: Mapped[int | None] = mapped_column(
        ForeignKey("credentials.id"),
        nullable=True
    )

    uid_lido: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )       

    device_id: Mapped[int] = mapped_column(
        ForeignKey("devices.id"),
        nullable=False
    )     

    door_id: Mapped[int] = mapped_column(
        ForeignKey("doors.id"),
        nullable=False
    )      

    resultado: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False
    )

    motivo: Mapped[AccessReason] = mapped_column(
        SQLEnum(AccessReason),
        nullable=False
    )

    data_hora: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    # Entidade-Filha
    credential: Mapped["Credential | None"] = relationship(
        back_populates="access_logs"   
    )
    door: Mapped["Door"] = relationship(
        back_populates="access_logs"
    )
    device: Mapped["Device"] = relationship(
        back_populates="access_logs"
    )