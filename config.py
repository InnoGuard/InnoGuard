"""AI for Online Child Violence app configuration."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Configuration from environment variables."""

    
    API_KEY = environ.get('API_KEY')
