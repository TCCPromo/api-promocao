from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from api_promo.core.configs import settings


class UsuarioEstabelecimentoModel(settings.DBBaseModel):
    __tablename__ = 'usuario_estabelecimento'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), nullable=False)
    estabelecimentos = relationship('EstabelecimentoModel', backref='usuario_estabelecimento', lazy='subquery')