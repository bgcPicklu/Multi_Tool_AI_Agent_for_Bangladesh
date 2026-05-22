import os
from dotenv import load_dotenv
from tavily import TavilyClient
from langchain.tools import tool

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

@tool("WebSearchTool")
def web_search(query: str) -> str:
    """
    Useful for answering general knowledge questions, definitions, policy checks, historical 
    events, or cultural contextual topics about Bangladesh that are not stored inside specific data rows.
    """
    if not api_key:
        return "Search tool error: TAVILY_API_KEY missing from system configurations."
        
    try:
        client = TavilyClient(api_key=api_key)
        # Fetching top results for richer context delivery
        response = client.search(query=query, max_results=3)
        results = response.get("results", [])
        
        if not results:
            return "No web search results matches found for this topic."
            
        compiled_context = []
        for idx, res in enumerate(results, 1):
            compiled_context.append(f"[{idx}] Source: {res.get('url')}\nContent: {res.get('content')}")
            
        return "\n\n".join(compiled_context)
    except Exception as e:
        return f"Web search runtime error: {str(e)}"