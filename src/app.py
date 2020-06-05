#src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt

# import fake_api blueprint
from .controllers.FakeController import fake_api


def create_app(env_name):
  """
  Create app
  """
  
  # app initialization
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  # initializing bcrypt and db
  bcrypt.init_app(app) # For authorization/encryption
  db.init_app(app)

  # setting up url groups endpoint for the controllers
  app.register_blueprint(fake_api, url_prefix='/api/v1/fake')

  # Routing goes here
  @app.route('/', methods=['GET'])
  def index():
    """
    example endpoint
    """
    # See docs on how to return various data types
    return 'Welcome to Python Flask Microservice API'

  # Run this function in run.py
  return app

