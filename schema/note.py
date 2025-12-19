"""Note serialization schemas.

This module provides functions to serialize MongoDB documents into Note objects.
"""

from typing import List, Dict, Any


def noteCreate(item: Dict[str, Any]) -> Dict[str, Any]:
    """Convert a MongoDB document to a Note dictionary.
    
    Args:
        item: MongoDB document containing note data
        
    Returns:
        Dictionary with note data including string ID
    """
    return {
        "id": str(item["_id"]),
        "title": item["title"],
        "description": item["description"],
        "important": item["important"]
    }


def Notes(items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert a list of MongoDB documents to Note dictionaries.
    
    Args:
        items: List of MongoDB documents
        
    Returns:
        List of note dictionaries
    """
    return [noteCreate(item) for item in items]
