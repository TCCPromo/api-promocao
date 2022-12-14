from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from api_promo.core.configs import settings


class UsuarioModel(settings.DBBaseModel):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), nullable=False)
    urlImagem = Column(String(256), nullable=True)
    pontuacao = Column(Integer, nullable=True)
    promocoes = relationship(
        "PromocaoModel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
    avaliacoes = relationship(
        "AvaliacaoModel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
    curtidas = relationship(
        "CurtidaModel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )
    conquistas = relationship(
        "UsuarioConquistaModel",
        cascade="all,delete-orphan",
        back_populates="criador",
        uselist=True,
        lazy="joined"
    )