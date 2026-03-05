from sqlalchemy.orm import Session
from . import models, schemas

def get_sources(db: Session):
    return db.query(models.Source).all()

def get_source(db: Session, source_id: int):
    return db.query(models.Source).filter(models.Source.id == source_id).first()

def create_source(db: Session, source: schemas.SourceCreate):
    db_source = models.Source(name=source.name, url=source.url)
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source

def update_source(db: Session, source_id: int, source: schemas.SourceCreate):
    db_source = get_source(db, source_id)
    if db_source:
        db_source.name = source.name
        db_source.url = source.url
        db.commit()
        db.refresh(db_source)
    return db_source

def delete_source(db: Session, source_id: int):
    db_source = get_source(db, source_id)
    if db_source:
        db.delete(db_source)
        db.commit()
    return db_source