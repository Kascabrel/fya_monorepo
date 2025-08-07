FROM python:3.12-slim

WORKDIR /app
ENV PYTHONPATH=/app

RUN pip install --no-cache-dir poetry

# Copie uniquement les fichiers nécessaires pour installer les deps
COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copier le reste du code
COPY . /app

EXPOSE 8000

# Le démarrage sera géré via docker-compose
