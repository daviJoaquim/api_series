from unittest import result

from fastapi import APIRouter, Depends, HTTPException, status 
from httpx import get
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.serie import SerieModel
from app.schema.serie import SerieSchema

serie = APIRouter()

@serie.post("/")
async def criar_serie(dados: SerieSchema, db: Session = Depends(get_db)):
    nova_serie = SerieModel(**dados.model_dump())
    db.add(nova_serie)
    db.commit()
    db.refresh(nova_serie)
    return nova_serie

@serie.get("/series")
async def listar_series(db:Session = Depends(get_db)):
    return db.query(SerieModel).all()

@serie.put('/update/{id}')
async def atualizar_serie(id: int, titulo: str, descricao: str, ano_lancamento: int):
    results = {'titulo': titulo, 'descrição': descricao, "Ano Lançamento": ano_lancamento}
    db.commit()
    db.refresh
    return results

@serie.delete("/deletar/{id}")
async def deletar_series(id: int, db:Session= Depends(get_db)):
    db.query(SerieModel).filter(SerieModel.id == id).first()

    if not id:
        return("Não foi localizado o id")
    db.delete(id)
    db.commit()
    return("Deletado")






# Tarefa 1: Resolva todos os erros da sua aplicação
# Tarefa 2: Crie as rotas de atualização e deleção da API
# Tarefa 3: Resolva todos os erros das novas rotas
# Versione

