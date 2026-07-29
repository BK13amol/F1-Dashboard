from sqlalchemy import text
from backend.database.connection import engine

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print(result.scalar())

    print("\nDatabase connected successfully!")

except Exception as e:
    print(e)
