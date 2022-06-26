from pydantic import BaseModel

# class Wiki(BaseModel):
#     title: str
#     body: str

class Wiki(BaseModel):
    id: str
    link: str
    meta: str
    judul: str
    abstrak: str
    sejarah: str
    jenis: str
    ketua: str
    wakil_ketua: str
    anggota: str
    periode: str
    alokasi_apbn: str
    logo: str
    situs_web: str