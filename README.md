# Product Browser API

## Tech Stack

- FastAPI
- PostgreSQL
- Psycopg2

## Features

- Browse 200,000 products
- Category filtering
- Cursor pagination
- High performance indexing

## Run

pip install -r requirements.txt

python scripts/seed.py

python -m uvicorn app.main:app --reload