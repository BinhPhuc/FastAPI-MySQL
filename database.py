from sqlmodel import SQLModel, create_engine
DATABASE_URL = "mysql+pymysql://root:binh2006@localhost:3306/heroapplication"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)