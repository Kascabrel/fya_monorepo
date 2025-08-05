# Utilise une image officielle Python
FROM python:3.11-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Installer Poetry
RUN pip install --no-cache-dir poetry

# Copier les fichiers de l’app
COPY pyproject.toml poetry.lock* /app/

# Installer les dépendances
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Copier le reste de l’application
COPY . /app

# Exposer le port de l'API
EXPOSE 8000

# Commande de démarrage
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
