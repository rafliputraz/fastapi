from typing import List
from fastapi import Depends, FastAPI, status, Response, HTTPException
import schemas, models, database
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(database.engine)

def get_db():
    db = database.LocalSession()
    try:
        yield db
    finally:
        db.close()

@app.post('/wiki')
async def create(request: schemas.Wiki, db: Session = Depends(get_db)):
    new_post = models.Wiki(
        id=request.id,
        link=request.link,
        meta=request.meta,
        judul=request.judul,
        abstrak=request.abstrak,
        sejarah=request.sejarah,
        jenis=request.jenis,
        ketua=request.ketua,
        wakil_ketua=request.wakil_ketua,
        anggota=request.anggota,
        periode=request.periode,
        alokasi_apbn=request.alokasi_apbn,
        logo=request.logo,
        situs_web=request.situs_web
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@app.delete('/wiki/{id}')
async def destroy(id, db: Session = Depends(get_db)):
    db.query(models.Wiki).filter(models.Wiki.id == id).delete(synchronize_session=False)
    db.commit()
    return 'deleted'

@app.put('/wiki/{id}')
async def update(id, request:schemas.Wiki, db: Session = Depends(get_db)):
    db.query(models.Wiki).filter(models.Wiki.id == id).update(request.dict())
    db.commit()
    return 'updated'


@app.get('/wiki')
async def all(db: Session = Depends(get_db)):
    wikis = db.query(models.Wiki).all()
    return wikis

@app.get('/wiki/{id}')
async def show(id, response: Response, db: Session = Depends(get_db)):
    wiki = db.query(models.Wiki).filter(models.Wiki.id == id).first()
    if not wiki:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return wiki


@app.get('/')
def index():
    return {'Hello': 'World'}