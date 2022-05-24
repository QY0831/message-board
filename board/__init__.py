
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

# app = Flask(__name__)
# normally use __name__ which is the .py name
# since we initialize the app object in init.py
# need specific the argument
# this argument is name of module or package
# flask will use this name to determine the location of static and templates resources

print("init app obj")
app = Flask('board')  # get resources in board package
app.config.from_pyfile('settings.py')  # import settings, such as db conn

# auto remove blank spaces in blocks in html
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# get db object
db = SQLAlchemy(app)

# get bootstrap templates
bootstrap = Bootstrap(app)

from board import views, commands, errors

# when import object from __init__.py
# don't have to 'from ..init import ...'
# just import from the package name
# such as
# from board import app
