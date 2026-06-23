# Product Browser API

## Tech Stack
- FastAPI
- PostgreSQL
- Psycopg2

## Features
- 200,000 products
- Category filtering
- Cursor pagination
- Indexed queries

## Run

pip install -r requirements.txt

python scripts/seed.py

python -m uvicorn app.main:app --reload