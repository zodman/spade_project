import os
from model import Person,Consult, ConsultExt, db

def create_tables():
    db.create_tables([Person,Consult,ConsultExt])

def init_data():
    d = Person.create(name="doc1",
        social_number="1", address="calle 30", 
        location="Yucatan", type="1")
    Person.create(name="Andres Vargas",
        social_number="2", address="calle 30", 
        location="Yucatan", type="1")
    Person.create(name="Andres Vargas2",
        social_number="3", address="calle 30", 
        location="Yucatan", type="1")
    p = Person.create(name="Andres Vargas3",
        social_number="4", address="calle 30", 
        location="Yucatan", type="1")
    c = Consult.create(paciente=p, doctor=d,
        sintomas="niguno", diagnostico="ninguno",
        tratamiento="none", notas=""
        )

if __name__ == "__main__":
    create_tables()
    init_data()
