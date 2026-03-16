from fastapi import APIRouter, Depends, HTTPException, status 
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

@serie.put("/series/{id}")
async def atualizar_series(id: int, dados: SerieSchema, db: Session = Depends(get_db)):
   serie = db.query(SerieModel).filter(SerieModel.id == id).first()

   if not serie: 
       raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Série com ID {id} não encontrada"
        )
   
   for campo, valor in dados.model_dump().items():
       setattr(serie, campo, valor)

   db.commit()
   db.refresh(serie)

   return serie

@serie.delete("/series/{id}/delete")
async def deletar_series(id: int, db:Session= Depends(get_db)):
    
    serie = db.query(SerieModel).filter(SerieModel.id == id).first()

    if not id:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail=f"A série com ID {id} não foi encontrada"
        )

        
    db.delete(serie)
    db.commit()
    return("Deletado com sucesso!")




# Tarefa 1: Resolva todos os erros da sua aplicação
# Tarefa 2: Crie as rotas de atualização e deleção da API
# Tarefa 3: Resolva todos os erros das novas rotas
# Versione

