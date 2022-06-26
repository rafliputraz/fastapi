from sqlalchemy import Integer, Column, String
from database import Base

class Wiki(Base):
    __tablename__ = 'wiki'
    id = Column(String, primary_key=True, index=True)
    link = Column(String)
    meta = Column(String)
    judul = Column(String)
    abstrak = Column(String)
    sejarah = Column(String)
    jenis = Column(String)
    ketua = Column(String)
    wakil_ketua = Column(String)
    anggota = Column(String)
    periode = Column(String)
    alokasi_apbn = Column(String)
    logo = Column(String)
    situs_web = Column(String)