# main.py - Main application file
import os

def load_configuration():
    """Loads configuration from environment variables."""
    api_key = os.getenv("API_KEY")
    db_url = os.getenv("DATABASE_URL")
    print("Configuration loaded.")
    return {"api_key": api_key, "db_url": db_url}

def main():
    """Main entry point for the application."""
    print("Starting application...")
    config = load_configuration()
    print("Application running with loaded config.")
    # In a real app, there would be more logic here.
    print("Application finished.")

if __name__ == "__main__":
    main() 