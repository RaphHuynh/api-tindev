import os

USER = os.environ.get("MYSQL_USER")
PASSWORD = os.environ.get("MYSQL_PASSWORD")
HOST = os.environ.get("MYSQL_HOST", default="localhost")
DATABASE = os.environ.get("MYSQL_DATABASE")
PORT = os.environ.get("MYSQL_PORT", default=3306)