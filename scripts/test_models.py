from backend.database.connection import SessionLocal
from backend.database.models import Team

session = SessionLocal()

try:
    teams = session.query(Team).all()
    print(f"Found {len(teams)} teams.")
finally:
    session.close()
