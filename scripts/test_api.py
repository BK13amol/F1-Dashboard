from pprint import pprint
from backend.api.client import OpenF1Client

client = OpenF1Client()

sessions = client.get_sessions(year=2025)

print(f"Total sessions: {len(sessions)}")
pprint(sessions[0])
