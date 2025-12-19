# Notes App

A modern, full-stack notes application built with FastAPI and MongoDB. Create, manage, and organize your notes with an intuitive web interface.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![MongoDB](https://img.shields.io/badge/MongoDB-5.0+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Features

- ✨ Create and manage notes with title and description
- 🎯 Mark notes as important
- 🗑️ Delete notes with a single click
- 📱 Responsive Bootstrap UI
- ⚡ Fast and lightweight FastAPI backend
- 🔄 Real-time updates without page refresh
- 🗄️ MongoDB database for reliable data storage

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **Frontend**: HTML, Bootstrap 5, JavaScript
- **Template Engine**: Jinja2

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- MongoDB 5.0 or higher
- pip (Python package manager)

## Quick Start

### Automated Setup (Recommended)

Run the automated setup script to get started quickly:

```bash
python setup.py
```

This script will:
- Check Python and MongoDB compatibility
- Create a virtual environment
- Install all dependencies
- Set up environment configuration
- Verify database connection

### Manual Setup

If you prefer to set up manually:

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Notes-App
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv

   # On Windows
   venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. **Ensure MongoDB is running**
   ```bash
   # MongoDB should be running on localhost:27017
   ```

6. **Run the application**
   ```bash
   python index.py
   # or
   uvicorn index:app --reload
   ```

The application will be available at `http://localhost:8000`

## Project Structure

```
Notes-App/
├── config/              # Configuration files
│   ├── __init__.py     # Package initialization
│   └── db.py           # Database connection configuration
├── model/              # Pydantic models
│   ├── __init__.py     # Package initialization
│   └── note.py         # Note model definition
├── routes/             # API routes
│   ├── __init__.py     # Package initialization
│   └── note.py         # Note-related endpoints
├── schema/             # Database schemas
│   ├── __init__.py     # Package initialization
│   └── note.py         # Note serialization schemas
├── static/             # Static files (CSS, JS, images)
│   └── style.css       # Custom styles
├── template/           # HTML templates
│   └── index.html      # Main application template
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
├── ARCHITECTURE.md     # System architecture documentation
├── CODE_OF_CONDUCT.md  # Community code of conduct
├── CONTRIBUTING.md     # Contribution guidelines
├── LICENSE             # MIT license
├── README.md          # This file
├── index.py           # Application entry point
├── requirements.txt   # Python dependencies
└── setup.py          # Automated setup script
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Display all notes |
| POST | `/` | Create a new note |
| POST | `/del/{item_id}` | Delete a note by ID |

## Usage

### Creating a Note

1. Fill in the title and description fields
2. Optionally check "important" to mark the note as important
3. Click "Submit" to save the note

### Deleting a Note

Click the "del" button next to any note to remove it from the database.

## Development

### Running in Development Mode

```bash
uvicorn index:app --reload --port 8000
```

### Database Schema

**Notes Collection:**
```json
{
  "_id": "ObjectId",
  "title": "string",
  "description": "string",
  "important": "boolean"
}
```

## Testing

To run tests, use the following command:
```bash
pytest
```
Ensure all tests pass before making changes.

## Deployment

To deploy the app to production:
1. Set up a production MongoDB instance.
2. Configure the `.env` file with production settings.
3. Use a production server like `gunicorn` or `uvicorn`:
   ```bash
   uvicorn index:app --host 0.0.0.0 --port 80
   ```

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details on:

- How to report bugs and suggest features
- Development setup and workflow
- Code style guidelines
- Pull request process

## Code of Conduct

This project follows a code of conduct to ensure a welcoming environment for all contributors. Please read our [Code of Conduct](CODE_OF_CONDUCT.md) before participating.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Documentation

- [Architecture Overview](ARCHITECTURE.md) - System design and data flow
- [Contributing Guide](CONTRIBUTING.md) - How to contribute to the project
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community guidelines

## Acknowledgments

- FastAPI for the excellent web framework
- MongoDB for the database
- Bootstrap for the UI components
- The open-source community for inspiration and tools

---

