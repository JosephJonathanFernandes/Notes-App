#!/usr/bin/env python3
"""
Setup script for Notes App development environment.

This script helps set up the development environment for the Notes App,
including creating virtual environment, installing dependencies, and
configuring basic settings.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path


def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during {description}: {e}")
        print(f"Error output: {e.stderr}")
        return None


def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    print(f"✅ Python version: {sys.version}")


def check_mongodb():
    """Check if MongoDB is installed and running."""
    try:
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
        client.admin.command('ping')
        print("✅ MongoDB is running and accessible")
        return True
    except Exception as e:
        print(f"⚠️  MongoDB check failed: {e}")
        print("   Please ensure MongoDB is installed and running on localhost:27017")
        return False


def create_virtual_environment():
    """Create a Python virtual environment."""
    if os.path.exists("venv"):
        print("ℹ️  Virtual environment already exists")
        return True

    return run_command("python -m venv venv", "Creating virtual environment") is not None


def activate_virtual_environment():
    """Get the path to the virtual environment's Python executable."""
    if os.name == 'nt':  # Windows
        python_exe = os.path.join("venv", "Scripts", "python.exe")
    else:  # Unix/Linux/macOS
        python_exe = os.path.join("venv", "bin", "python")

    return python_exe


def install_dependencies():
    """Install Python dependencies."""
    python_exe = activate_virtual_environment()

    # Upgrade pip first
    run_command(f'"{python_exe}" -m pip install --upgrade pip',
                "Upgrading pip")

    # Install dependencies
    result = run_command(f'"{python_exe}" -m pip install -r requirements.txt',
                        "Installing dependencies")
    return result is not None


def create_env_file():
    """Create .env file from .env.example if it doesn't exist."""
    if os.path.exists(".env"):
        print("ℹ️  .env file already exists")
        return True

    if os.path.exists(".env.example"):
        shutil.copy(".env.example", ".env")
        print("✅ Created .env file from .env.example")
        print("   Please edit .env file with your configuration")
        return True
    else:
        print("⚠️  .env.example not found")
        return False


def run_initial_setup():
    """Run initial database setup if needed."""
    python_exe = activate_virtual_environment()

    print("🔧 Running initial setup...")
    try:
        result = subprocess.run([python_exe, "-c", """
import os
from dotenv import load_dotenv
from config.db import conn

load_dotenv()
db_name = os.getenv('DATABASE_NAME', 'notes')
print(f"Database '{db_name}' is ready for use")
"""], capture_output=True, text=True, check=True)
        print("✅ Database connection verified")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Database setup failed: {e}")
        print(f"Error output: {e.stderr}")
        return False


def main():
    """Main setup function."""
    print("🚀 Setting up Notes App development environment")
    print("=" * 50)

    # Check Python version
    check_python_version()

    # Check MongoDB
    mongodb_ok = check_mongodb()

    # Create virtual environment
    if not create_virtual_environment():
        sys.exit(1)

    # Install dependencies
    if not install_dependencies():
        sys.exit(1)

    # Create .env file
    create_env_file()

    # Run initial setup
    if mongodb_ok:
        run_initial_setup()

    print("\n" + "=" * 50)
    print("🎉 Setup completed!")
    print("\nTo activate the virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("\nTo run the application:")
    print("   python index.py")
    print("   or")
    print("   uvicorn index:app --reload")
    print("\nFor more information, see README.md")


if __name__ == "__main__":
    main()
