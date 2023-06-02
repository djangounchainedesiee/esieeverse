# Utiliser l'image de base Python 3.9.13
FROM python:3.9.13

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de configuration et les dépendances du projet
COPY requirements.txt .

# Installer les dépendances du projet
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source du projet dans le conteneur
COPY . .

# Définir les variables d'environnement
ENV DJANGO_DEBUG=False
ENV DJANGO_SETTINGS_MODULE=esieeverse.settings.production

# Exposer le port utilisé par votre application Django (par exemple, le port 8000)
EXPOSE 8000

# Lancer le serveur Django avec Gunicorn
CMD ["gunicorn", "esieeverse.wsgi:application", "--bind", "0.0.0.0:8000"]