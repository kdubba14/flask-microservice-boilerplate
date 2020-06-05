from python:3

MAINTAINER BugFunction

COPY . /app
WORKDIR /app

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["python", "run.py"]