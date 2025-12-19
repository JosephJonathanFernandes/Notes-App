"""Note model definition.

This module defines the Pydantic model for Note objects.
"""

from pydantic import BaseModel, validator
from typing import Optional


class Note(BaseModel):
    """Note model for creating and validating note data.

    Attributes:
        title: The title of the note
        description: The detailed description of the note
        important: Flag indicating if the note is marked as important
    """
    title: str
    description: str
    important: Optional[bool] = False

    @validator('title')
    def title_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Title must not be empty')
        if len(v) > 200:
            raise ValueError('Title must be less than 200 characters')
        return v

    @validator('description')
    def description_must_not_be_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('Description must not be empty')
        if len(v) > 1000:
            raise ValueError('Description must be less than 1000 characters')
        return v

    class Config:
        schema_extra = {
            "example": {
                "title": "Sample Note",
                "description": "This is a sample note description",
                "important": False
            }
        }

