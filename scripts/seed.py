from dotenv import load_dotenv
import os
from faker import Faker
import random
import psycopg2
from psycopg2.extras import execute_values
from datetime import datetime
import time

# Load environment variables
load_dotenv()

# Start timer
start_time = time.time()

# Faker instance
fake = Faker()

# Database connection
DATABASE_URL = os.getenv("DATABASE_URL")

print("Connecting to database...")
conn = psycopg2.connect(DATABASE_URL)

cursor = conn.cursor()

# Categories
categories = [
    "Electronics",
    "Books",
    "Sports",
    "Fashion",
    "Home"
]

# 10,000 records per batch
batch_size = 10000

# 20 batches = 200,000 products
for batch in range(20):

    products = []

    for _ in range(batch_size):

        products.append(
            (
                fake.word(),
                random.choice(categories),
                random.randint(100, 50000),
                datetime.now(),
                datetime.now()
            )
        )

    # FAST INSERT
    execute_values(
        cursor,
        """
        INSERT INTO products
        (
            name,
            category,
            price,
            created_at,
            updated_at
        )
        VALUES %s
        """,
        products
    )

    conn.commit()

    print(
        f"Batch {batch + 1}/20 inserted "
        f"({(batch + 1) * batch_size:,} records)"
    )

cursor.close()
conn.close()

print(
    f"\n 200,000 products inserted successfully "
    f"in {(time.time() - start_time):.2f} seconds"
)