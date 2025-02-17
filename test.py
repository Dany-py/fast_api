from sqlalchemy import create_engine

engine = create_engine("postgresql+asyncpg://postgres:040501@localhost:5432/JeroTest")
with engine.connect() as conn:
    result = conn.execute("SELECT tablename FROM pg_tables WHERE schemaname='public'")
    print(result.fetchall())
