from typing import Optional

from pydantic import BaseModel
from typing import Optional
from typing import List
from sqlalchemy import BigInteger

from api_promo.schemas.departamento_schema import DepartamentoSchema


class ProdutoSchema(BaseModel):
    id: Optional[int] = None
    ean: str
    nome: str
    marca: Optional[str]
    departamento_id: Optional[int] = None
    urlImagem: Optional[str]

    class Config:
        orm_mode = True

class ProdutoSchemaAlter(BaseModel):
    id: Optional[int] = None
    ean: Optional[str]
    nome: Optional[str]
    marca: Optional[str]
    departamento_id: Optional[int] = None
    urlImagem: Optional[str]

    class Config:
        orm_mode = True

class ProdutoSchemaCompleto(BaseModel):
    id: Optional[int] = None
    ean: str
    nome: str
    marca: Optional[str]
    urlImagem: Optional[str]
    departamentos: Optional[DepartamentoSchema]

    class Config:
        orm_mode = True
