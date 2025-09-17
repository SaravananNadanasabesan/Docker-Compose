from flask import Flask 
from sqlalchemy import create_engine, text
import redis
import os

app = Flask(__name__)

# Read environment variables from docker-compose
DB_HOST = os.getenv("DB_HOST", "database")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "password")
DB_NAME = os.getenv("DB_NAME", "mydb")   # 🔹 Updated to match docker-compose

CACHE_HOST = os.getenv("CACHE_HOST", "cache")
CACHE_PORT = os.getenv("CACHE_PORT", "6379")

# Connect to PostgreSQL using SQLAlchemy
db_url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(db_url, pool_pre_ping=True)

# Connect to Redis
r = redis.Redis(host=CACHE_HOST, port=int(CACHE_PORT))

@app.route('/')
def hello():
    try:
        # Redis counter
        visits = r.incr("counter")
    except Exception as e:
        visits = f"Redis error: {e}"

    try:
        # Get current time from DB
        with engine.connect() as conn:
            result = conn.execute(text("SELECT NOW()"))
            db_time = result.fetchone()[0]
    except Exception as e:
        db_time = f"DB error: {e}"

    # Combine "Hello, World!" with backend info
    return (
        f"Hello, World!<br>"
        f"DB Time: {db_time}<br>"
        f"Visit Count (via Redis): {visits}"
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
