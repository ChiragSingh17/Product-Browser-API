from faker import Faker
import random
import psycopg2
from datetime import datetime

fake = Faker()

conn = psycopg2.connect(
    database="product_db",
    user="postgres",
    password="Chirag",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

categories = [
    "Electronics",
    "Books",
    "Sports",
    "Fashion",
    "Home"
]

batch_size = 10000

for batch in range(20):

    products = []

    for i in range(batch_size):

        products.append(
            (
                fake.word(),
                random.choice(categories),
                random.randint(100,50000),
                datetime.now(),
                datetime.now()
            )
        )

    cursor.executemany(
        """
        INSERT INTO products
        (
            name,
            category,
            price,
            created_at,
            updated_at
        )
        VALUES (%s,%s,%s,%s,%s)
        """,
        products
    )

    conn.commit()

    print(f"Batch {batch+1} inserted")

cursor.close()
conn.close()

print("200000 products inserted")