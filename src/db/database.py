from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:binh2006@localhost:3306/heroapplication"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session