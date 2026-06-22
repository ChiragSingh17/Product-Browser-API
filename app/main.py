from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get("/products")
def get_products(
    category: str = None,
    cursor_id: int = None,
    cursor_updated_at: str = None
    ):

    conn = psycopg2.connect(
        database="product_db",
        user="postgres",
        password="Chirag",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

     # First page
    if cursor_id is None or cursor_updated_at is None:

        if category:
            cursor.execute("""
                SELECT *
                FROM products
                WHERE category = %s
                ORDER BY updated_at DESC, id DESC
                LIMIT 20
            """, (category,))
        else:
            cursor.execute("""
                SELECT *
                FROM products
                ORDER BY updated_at DESC, id DESC
                LIMIT 20
            """)

    # Next page
    else:

        if category:
            cursor.execute("""
                SELECT *
                FROM products
                WHERE category = %s
                AND (updated_at, id) < (%s, %s)
                ORDER BY updated_at DESC, id DESC
                LIMIT 20
            """, (category, cursor_updated_at, cursor_id))
        else:
            cursor.execute("""
                SELECT *
                FROM products
                WHERE (updated_at, id) < (%s, %s)
                ORDER BY updated_at DESC, id DESC
                LIMIT 20
            """, (cursor_updated_at, cursor_id))
        
    products = cursor.fetchall()

    next_cursor = None

    if products:
        last_product = products[-1]

        next_cursor = {
         "id": last_product[0],
            "updated_at": str(last_product[5])
    }

    return {
     "products": products,
     "next_cursor": next_cursor
}