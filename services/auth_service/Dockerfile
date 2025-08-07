# Image Python slim
FROM python:3.12-slim

# Créer le dossier app
WORKDIR /app/services/auth_service
ENV PYTHONPATH=/app

# Installer Poetry
RUN pip install --no-cache-dir poetry

# Copier uniquement les fichiers nécessaires à l’installation (pour la couche de cache Docker)
COPY pyproject.toml poetry.lock* /app/

# Installer les dépendances
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction --no-ansi

# Exposer le port
EXPOSE 8000

# Lancement automatique géré par docker-compose via `command`
