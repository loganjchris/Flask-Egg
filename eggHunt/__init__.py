from flask import Flask
import os, config
 
# create application instance
eggHunt = Flask(__name__)
eggHunt.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')


# import views
from . import views
