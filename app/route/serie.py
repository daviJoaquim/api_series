from unittest import result

from fastapi import APIRouter, Depends, HTTPException, status 
from sqlalchemy import Update
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

@serie.put("/update/{id}")
async def atualizar_series(id: int, dados: SerieSchema ,db:Session= Depends(get_db)):
   serie = db.query(SerieModel).filter(SerieModel.id == id).first()

   if not serie:
            return("Série não foi encontrada")
   
   db.query(SerieModel).filter(SerieModel.id == id).update(dados.model_dump(exclude_unset=True))
   db.commit()
   return (dados)


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

