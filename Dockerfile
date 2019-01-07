FROM python:latest

WORKDIR /usr/local/app
ADD Pipfile.lock .
RUN pip install pipenv && \
    pipenv install --ignore-pipfile -d

ENTRYPOINT ["pipenv", "run"]