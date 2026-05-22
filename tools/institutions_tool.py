import sqlite3
from utils.text_utils import normalize

def query_institutions(question: str):

    conn = sqlite3.connect("databases/institutions.db")
    cursor = conn.cursor()

    q = normalize(question)
    # cursor.execute("PRAGMA table_info(institutions)")
    # print(cursor.fetchall())

    if "rajshahi" in q:

        cursor.execute("""
            SELECT "INSTITUTE NAME", DISTRICT, INSTITUTE_TYPE, ADDRESS
            FROM institutions
            WHERE LOWER(DISTRICT) LIKE '%rajshahi%'
            LIMIT 10
        """)

        rows = cursor.fetchall()

        if rows:
            return "Institutions in Rajshahi:\n" + "\n".join([r[0] for r in rows])

        return "No institutions found in Rajshahi"

    return "No matching institution data found."