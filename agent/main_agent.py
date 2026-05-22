import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from utils.text_utils import normalize

# Import custom engineered tools directly
from tools.db_tools import query_hospitals, query_restaurants, query_institutions
from tools.web_search_tool import web_search

load_dotenv()

groq_key = os.getenv("GROQ_API_KEY")
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY missing from environment variables.")

# Lightweight LLM to cleanly synthesize unstructured web data layouts
llm = ChatGroq(
    temperature=0.1, 
    model_name="llama-3.1-8b-instant",  
    groq_api_key=groq_key
)

def ask_agent(query: str) -> str:
    """
    Deterministic Router Agent: Smart routing structure that selects between
    local summary DB lookups and high-fidelity real-time web compilation.
    """
    normalized_query = normalize(query).lower()
    
    try:
        # 1. Routing Rule: Educational Institutions
        if any(kw in normalized_query for kw in ["university", "universities", "college", "colleges", "school", "institute"]):
            return query_institutions.run(query)
            
        # 2. Routing Rule: Restaurants (with corrected conditional fallback)
        elif any(kw in normalized_query for kw in ["restaurant", "restaurants", "eatery", "cafe", "dine", "cuisine", "food"]):
            # EDGE CASE: If they are searching for specific dishes, a top-rated list, or specific regional spots like Chittagong,
            # use the web fallback instead of hitting the basic static local DB sample.
            if any(food_kw in normalized_query for food_kw in ["biryani", "kacchi", "burger", "pizza", "best", "top", "find", "chittagong", "chattogram", "sylhet", "khulna"]):
                return execute_web_fallback(query)
            # Otherwise, use the fast local database query
            return query_restaurants.run(query)
            
        # 3. Routing Rule: Hospitals
        elif any(kw in normalized_query for kw in ["hospital", "hospitals", "clinic", "medical center"]):
            # EDGE CASE: If they want a list, ranking, or specific comparative capacities, use search for full depth
            if any(lk in normalized_query for lk in ["list", "top", "rank", "best", "names of", "bed capacity", "capacities"]):
                return execute_web_fallback(query)
            # Otherwise, use the fast local statistical count tool
            return query_hospitals.run(query)
            
        # 4. Default Fallback Routing Rule: Web Search
        else:
            return execute_web_fallback(query)

    except Exception as e:
        return f"An operational error occurred during processing: {str(e)}"

def execute_web_fallback(query: str) -> str:
    """Helper method to execute a clean open-web search synthesis turn."""
    search_context = web_search.run(query)
    
    synthesis_prompt = f"""You are a helpful assistant providing information about Bangladesh.
Based on the following real-time web search results, provide a clear, concise, and beautifully structured final answer to the user's question.

User Question: {query}
Search Results: {search_context}

Final Answer:"""
    
    response = llm.invoke(synthesis_prompt)
    return response.content