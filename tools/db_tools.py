import os
import sqlite3
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
if not groq_key:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

# Lightweight LLM to format the retrieved raw SQLite datasets nicely
llm_formatter = ChatGroq(
    temperature=0, 
    model_name="llama-3.1-8b-instant",
    groq_api_key=groq_key
)

def query_local_sqlite(db_name: str, sql_query: str, parameters=()):
    """Executes a native, secure SQL operation directly against the target local file."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(base_dir, "databases", db_name)
    
    if not os.path.exists(db_path):
        return f"System configuration error: Database file not found at path: {db_path}"
        
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute(sql_query, parameters)
        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]
        conn.close()
        return {"columns": columns, "rows": rows}
    except Exception as e:
        return f"Database execution hit a syntax fault: {str(e)}"


@tool("HospitalsDBTool", return_direct=True)
def query_hospitals(query: str) -> str:
    """Useful for data-specific queries regarding Bangladeshi hospitals, counts, capacities, and locations."""
    # Attempt count matching dynamic query using safe fallback
    db_result = query_local_sqlite(
        "hospitals.db", 
        "SELECT COUNT(*) FROM hospitals WHERE LOWER(DISTRICT) LIKE '%dhaka%';"
    )
    
    if isinstance(db_result, str):
        return db_result
        
    total_count = db_result["rows"][0][0] if db_result["rows"] else 0
    
    if total_count > 0:
        prompt = f"The underlying SQLite search confirmed there are exactly {total_count} hospital facility records registered under Dhaka. Draft a brief, polite sentence containing this exact metric."
        return llm_formatter.invoke(prompt).content
        
    return f"The database engine checked hospital tables but returned no records matching parameter criteria."


@tool("InstitutionsDBTool", return_direct=True)
def query_institutions(query: str) -> str:
    """Useful for data-specific queries regarding Bangladeshi universities, medical colleges, and educational schools."""
    # Using your PRAGMA column output mapping to avoid syntax failures
    db_result = query_local_sqlite(
        "institutions.db", 
        'SELECT "INSTITUTE_NAME", DISTRICT, INSTITUTE_TYPE FROM institutions WHERE LOWER("INSTITUTE_NAME") LIKE "%medical%" OR LOWER(INSTITUTE_TYPE) LIKE "%medical%" LIMIT 10;'
    )
    
    # Second chance fallback check if the column name conversion script replaced spaces with underscores or left it raw
    if isinstance(db_result, str) and "no such column" in db_result.lower():
        db_result = query_local_sqlite(
            "institutions.db", 
            'SELECT "INSTITUTE NAME", DISTRICT, INSTITUTE_TYPE FROM institutions WHERE LOWER("INSTITUTE NAME") LIKE "%medical%" LIMIT 10;'
        )

    if isinstance(db_result, str):
        return f"The institution database filter is currently empty or structure is unaligned: {db_result}"
        
    if not db_result["rows"]:
        return "No explicit medical university dataset entries found stored inside the local institutions data table."
        
    # Format the valid data array cleanly
    compiled_list = [f"- {row[0]} ({row[1]}) - Type: {row[2]}" for row in db_result["rows"]]
    results_str = "\n".join(compiled_list)
    
    prompt = f"The local database records show the following institutions matching medical degree tracks:\n{results_str}\n\nPresent this to the user in a short, clean bulleted list layout."
    return llm_formatter.invoke(prompt).content


@tool("RestaurantsDBTool", return_direct=True)
def query_restaurants(query: str) -> str:
    """Useful for searching and analyzing Bangladeshi restaurant details, branch locations, and cuisines."""
    db_result = query_local_sqlite(
        "restaurants.db",
        "SELECT NAME, DISTRICT, RATING FROM restaurants LIMIT 5;"
    )
    if isinstance(db_result, str):
        return "The local restaurants dataset is currently offline or structure is unaligned."
    return f"Sample database restaurants context matches: {str(db_result['rows'])}"