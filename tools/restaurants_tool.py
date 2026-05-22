import sqlite3
from utils.text_utils import normalize

def query_restaurants(question: str):

    conn = sqlite3.connect("databases/restaurants.db")
    cursor = conn.cursor()

    q = normalize(question)

    # normalize
    if "chittagong" in q:
        q = q.replace("chittagong", "chattogram")

    if "chattogram" in q or "dhaka" in q:

        city = "Chattogram" if "chattogram" in q else "Dhaka"

        if "biryani" in q:
            cursor.execute("""
                SELECT name
                FROM restaurants
                WHERE LOWER(address) LIKE ?
                AND LOWER(name) LIKE '%biryani%'
                LIMIT 10
            """, (f"%{city.lower()}%",))

        else:
            cursor.execute("""
                SELECT name
                FROM restaurants
                WHERE LOWER(address) LIKE ?
                LIMIT 10
            """, (f"%{city.lower()}%",))

        rows = cursor.fetchall()

        if rows:
            return f"Restaurants in {city}:\n" + "\n".join([r[0] for r in rows])

        return f"No restaurants found in {city}"

    return "No matching restaurant data found."