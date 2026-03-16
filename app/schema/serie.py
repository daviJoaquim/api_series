#modelo de validação de dados Pydantic
from pydantic import BaseModel
from typing import Optional

from app.database import Base

class SerieSchema(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    ano_lancamento: int

    class Config:
        from_attributes = True

