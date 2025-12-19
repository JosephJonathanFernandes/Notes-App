# Architecture Documentation

## System Overview

The Notes App is a web-based application built using the FastAPI framework with MongoDB as the backend database. It follows a clean architecture pattern with separation of concerns.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                        Client Layer                          │
│  (Browser - HTML, CSS, JavaScript, Bootstrap)                │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP/HTTPS
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    Application Layer                         │
│                      (FastAPI)                               │
│  ┌─────────────────────────────────────────────────────┐    │
│  │            Routes (API Endpoints)                    │    │
│  │  - GET /  (Display all notes)                       │    │
│  │  - POST / (Create note)                             │    │
│  │  - POST /del/{id} (Delete note)                     │    │
│  └─────────────────────────────────────────────────────┘    │
│                       │                                       │
│  ┌─────────────────────────────────────────────────────┐    │
│  │         Business Logic Layer                         │    │
│  │  - Models (Pydantic validation)                     │    │
│  │  - Schemas (Data transformation)                    │    │
│  └─────────────────────────────────────────────────────┘    │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    Database Layer                            │
│                     (MongoDB)                                │
│  Database: notes                                             │
│  Collection: notes                                           │
│    - _id: ObjectId                                           │
│    - title: String                                           │
│    - description: String                                     │
│    - important: Boolean                                      │
└─────────────────────────────────────────────────────────────┘
```

## Component Description

### 1. Application Entry Point (`index.py`)
- Initializes the FastAPI application
- Configures middleware (CORS)
- Mounts static files
- Includes route handlers
- Manages application lifecycle events

### 2. Configuration Layer (`config/`)
- **db.py**: Database connection management
  - Loads environment variables
  - Creates MongoDB client
  - Manages database connections

### 3. Data Models (`model/`)
- **note.py**: Pydantic models for data validation
  - Defines Note structure
  - Validates input data
  - Provides type safety

### 4. Routing Layer (`routes/`)
- **note.py**: API endpoint handlers
  - Handles HTTP requests
  - Processes form data
  - Manages business logic
  - Returns responses (HTML/JSON)

### 5. Schema Layer (`schema/`)
- **note.py**: Data transformation functions
  - Converts MongoDB documents to dictionaries
  - Serializes ObjectId to strings
  - Prepares data for API responses

### 6. Presentation Layer (`template/`, `static/`)
- **template/index.html**: Main UI template
  - Displays notes list
  - Provides note creation form
  - Handles delete operations via JavaScript
- **static/style.css**: Custom styles

## Data Flow

### Creating a Note
1. User fills form in browser
2. Form submitted via POST to `/`
3. FastAPI receives request
4. Form data extracted and validated
5. Data inserted into MongoDB
6. User redirected to home page
7. All notes displayed

### Deleting a Note
1. User clicks delete button
2. JavaScript sends POST request to `/del/{id}`
3. FastAPI validates ObjectId
4. Note deleted from MongoDB
5. User redirected to home page
6. Updated notes list displayed

### Viewing Notes
1. User visits `/`
2. FastAPI queries MongoDB
3. Documents retrieved and transformed
4. Data passed to Jinja2 template
5. HTML rendered and sent to browser

## Security Considerations

- Input validation via Pydantic models
- ObjectId validation to prevent injection
- CORS middleware for cross-origin requests
- Environment variables for sensitive config

## Scalability Considerations

- Stateless application design
- MongoDB connection pooling
- Async/await for non-blocking operations
- Static file serving via CDN (recommended)

## Future Enhancements

- User authentication and authorization
- Note categories/tags
- Full-text search
- Rich text editor
- Note sharing
- API rate limiting
- Caching layer (Redis)
- Comprehensive test suite
