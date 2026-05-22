import sqlite3
from utils.text_utils import normalize

def query_hospitals(question: str):

    conn = sqlite3.connect("databases/hospitals.db")
    cursor = conn.cursor()

    q = normalize(question)

    # normalize city names
    if "chittagong" in q:
        q = q.replace("chittagong", "chattogram")

    if "dhaka" in q:

        if "how many" in q:
            cursor.execute("""
                SELECT COUNT(*)
                FROM hospitals
                WHERE LOWER(District) LIKE '%dhaka%'
            """)
            count = cursor.fetchone()[0]

            return f"Total hospitals in Dhaka: {count}"

        else:
            cursor.execute("""
                SELECT Name
                FROM hospitals
                WHERE LOWER(District) LIKE '%dhaka%'
                LIMIT 10
            """)
            rows = cursor.fetchall()

            return "Hospitals in Dhaka:\n" + "\n".join([r[0] for r in rows])

    return "No hospital data found for this location."