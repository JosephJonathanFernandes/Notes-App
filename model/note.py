"""Note model definition.

This module defines the Pydantic model for Note objects.
"""

from pydantic import BaseModel, Field
from typing import Optional


class Note(BaseModel):
    """Note model for creating and validating note data.
    
    Attributes:
        title: The title of the note
        description: The detailed description of the note
        important: Flag indicating if the note is marked as important
    """
    title: str = Field(..., min_length=1, max_length=200, description="Note title")
    description: str = Field(..., min_length=1, max_length=1000, description="Note description")
    important: bool = Field(default=False, description="Important flag")

