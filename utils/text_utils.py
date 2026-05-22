def normalize(text: str) -> str:
    """Normalize spelling variants typical to Bangladesh region configurations."""
    if not text:
        return ""
    
    text_lower = text.lower()
    
    # Map historic names to modern dataset representations
    if "chittagong" in text_lower:
        text_lower = text_lower.replace("chittagong", "chattogram")
        
    return text_lower