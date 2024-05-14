from fastapi import FastAPI, HTTPException, Depends
from typing import Annotated, List # https://wikidocs.net/194289
from sqlalchemy.orm import Session 
from pydantic import BaseModel 
from database import SessionLocal, engine 
import models 
from fastapi.middleware.cors import CORSMiddleware # react - FastAPI Cors Error 
import uvicorn

app = FastAPI()

# port 3001
origins = [
    'http://localhost:3001'
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
)

# Transaction Model 
class TransactionBase(BaseModel): # 
    amount: float
    category: str
    description: str
    is_income: bool
    date: str


class TransactionModel(TransactionBase):
    id: int 
    
    class Config: 
        orm_mode = True
        
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close() # request가 반환되어야 하는 동안에만 db를 열어둔다. 
    
# dependency injection
db_dependency = Annotated[Session, Depends(get_db)]

# create table, Column Automatically 
models.Base.metadata.create_all(bind=engine)

@app.post("/transactions/", response_model=TransactionModel)
async def create_transaction(transaction: TransactionBase, db: db_dependency):
    db_transaction = models.Transaction(**transaction.dict())
    db.add(db_transaction)
    db.commit() 
    db.refresh(db_transaction)
    return db_transaction 

@app.get("/transactions", response_model=List[TransactionModel])
async def read_transactions(db: db_dependency, skip: int = 0, limit: int = 100):
    transactions = db.query(models.Transaction).offset(skip).limit(limit).all()
    return transactions

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=3001, log_level="info")
    # (env) > python main.py