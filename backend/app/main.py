# backend/app/main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from . import models, schemas, crud
from fastapi.middleware.cors import CORSMiddleware
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://user:password@db:5432/news")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Убираем создание таблиц из глобальной области
# models.Base.metadata.create_all(bind=engine)  <-- удалить

app = FastAPI(title="News Sources API")

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Server is running"}

@app.post("/sources/", response_model=schemas.Source)
def create_source(source: schemas.SourceCreate, db: Session = Depends(get_db)):
    return crud.create_source(db, source)

@app.get("/sources/", response_model=list[schemas.Source])
def read_sources(db: Session = Depends(get_db)):
    return crud.get_sources(db)

@app.put("/sources/{source_id}", response_model=schemas.Source)
def update_source(source_id: int, source: schemas.SourceCreate, db: Session = Depends(get_db)):
    db_source = crud.update_source(db, source_id, source)
    if not db_source:
        raise HTTPException(status_code=404, detail="Source not found")
    return db_source

@app.delete("/sources/{source_id}")
def delete_source(source_id: int, db: Session = Depends(get_db)):
    db_source = crud.delete_source(db, source_id)
    if not db_source:
        raise HTTPException(status_code=404, detail="Source not found")
    return {"ok": True}

# Создание таблиц ТОЛЬКО если запускаем main.py напрямую
if __name__ == "__main__":
    models.Base.metadata.create_all(bind=engine)