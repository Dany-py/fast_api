from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "postgresql+asyncpg://postgres:040501@0.0.0.0:5432/test"

# Création du moteur asynchrone
engine = create_async_engine(DATABASE_URL, echo=True)

# Création de la session
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Base pour les modèles
Base = declarative_base()

# Dépendance pour récupérer la session
async def get_db():
    async with SessionLocal() as session:
        yield session
