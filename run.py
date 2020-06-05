# /run.py
import os
from dotenv import load_dotenv, find_dotenv

from src.app import create_app

# loading variables from .env file
load_dotenv(find_dotenv())

# getting 'BUILD_ENV' environment variable (not required)
env_name = os.getenv('BUILD_ENV')
# creating app instance
app = create_app(env_name)

#  Runs the app (starts the server [optional PORT selection via env variable])
if __name__ == '__main__':
  port = os.getenv('PORT')
  # run app
  app.run(host='0.0.0.0', port=port)
