# Python Flask REST Microservice 

REST API written in Python Flask using SQLAlchemy as the ORM with auto migration capabilities

## Pre-requisites
  - Download & install [Python 3.6 or higher](https://www.python.org/downloads/)
  - Download & install [Pipenv](https://docs.pipenv.org/)
   ```bash
    python -m pip install -U pip 
   ```

## For Developers
  - Download & install [NodeJS](https://nodejs.org/en/download/) 
  - Install nodemon (use sudo if you in linux)
  ```bash
  npm i -g nodemon
  ```

## Installation

  ```bash
  # Change into the directory
  cd fake-microservice
  # Install all required dependencies with
  pipenv install pylint --dev
  # Activate the project virtual environment
  pipenv shell
  # Create an local .env file and replace with the relevant values
  cp .env.sample .env
  ```
  You can also set the enviroment variables explicity (OPTIONAL)
  
  ```bash
  PORT=9400
  BUILD_ENV=development
  DATABASE_URL=postgres://name:password@host:port/dbname
  ```

## Running the application

  **Start the app**
  ```bash
  python run.py
  ```
  **Start the app for developers**
  ```bash
  nodemon run.py
  ```

## Author

Bug Function