"""Utility functions for validation."""

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import HTTPException, status

def validate_object_id(item_id: str) -> ObjectId:
    """Validate and convert a string to a MongoDB ObjectId.

    Args:
        item_id: The string representation of the ObjectId.

    Returns:
        A valid ObjectId instance.

    Raises:
        HTTPException: If the ID is invalid.
    """
    try:
        return ObjectId(item_id)
    except InvalidId:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid note ID format"
        )