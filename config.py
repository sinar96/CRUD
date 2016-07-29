""" Configuration File """
import os

# Development (Debug -> True)
DEBUG =True
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))

SQLALCHEMY_DATABASE_URI = 'mysql://sinar96:sinar123@localhost/absen'
