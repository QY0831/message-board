import os
import sys
import re

# to support different OS
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

# set sqlite db file location
dirname, filename = os.path.split(os.path.abspath(__file__))
sqlite_db_url = prefix + os.path.join(dirname, 'data.db')

# get SECRET_KEY and SQLALCHEMY_DATABASE_URI from env if set
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', sqlite_db_url)

# close warning info while modifying db object
SQLALCHEMY_TRACK_MODIFICATIONS = False
