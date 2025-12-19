"""Database configuration module.

This module handles the MongoDB connection and database configuration.
"""

import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB Configuration
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "notes")

# Create MongoDB client connection
conn = MongoClient(MONGO_URL)
