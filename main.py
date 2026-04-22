
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel, EmailStr, Field

DATABASE_URL = "postgresql://postgres:abc%40264%40def@localhost:5432/hospital_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

app = FastAPI()


class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    specialization = Column(String)
    email = Column(String, unique=True)
    is_active = Column(Boolean, default=True)

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    phone = Column(String)

Base.metadata.create_all(bind=engine)


class DoctorCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True

class PatientCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
    phone: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/doctors")
def create_doctor(doctor: DoctorCreate, db: Session = Depends(get_db)):
    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

@app.get("/doctors")
def get_doctors(db: Session = Depends(get_db)):
    return db.query(Doctor).all()

@app.get("/doctors/{doctor_id}")
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = db.query(Doctor).filter(Doctor.id == doctor_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@app.post("/patients")
def create_patient(patient: PatientCreate, db: Session = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

@app.get("/patients")
def get_patients(db: Session = Depends(get_db)):
    return db.query(Patient).all()

