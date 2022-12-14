from sqlalchemy import Integer, String, Column, ForeignKey, UniqueConstraint 
from sqlalchemy.orm import relationship

from api_promo.core.configs import settings


class ProdutoModel(settings.DBBaseModel):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ean = Column(String(256), nullable=False)
    nome = Column(String(256), nullable=False)
    marca = Column(String(256), nullable=True)
    urlImagem = Column(String(256), nullable=True)
    departamento_id = Column(Integer, ForeignKey('departamento.id'))
    promocoes = relationship("PromocaoModel", back_populates="produto")
    departamentos = relationship("DepartamentoModel", back_populates="produtos", lazy='joined')