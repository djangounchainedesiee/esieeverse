# ESIEEVERSE

A collection of tools to help you manage your ESIEE Paris student life : 
- Social Network with Chat, Events, Groups, etc.
and more to come !

## Project Structure

The ESIEEVERSE project follows the following directory structure:

- .github : CI/CD files for github
- api/: Django rest framework application for api
- authentification/: Django application for user authentication and authorization.
- esieechat/: Django application for chat functionality.
- home/: Django application for the home page and general site functionality.
- profil/: Django application for user profiles.
- profilSetting/: Django application for user profile settings.
- publication/: Django application for user posts and publications.
- media/: Directory to store user-uploaded media files.
- staticfiles/: Directory to store static files used by the application.
- Dockerfile: Configuration file for building the Docker image.
- requirements.txt: File containing the Python dependencies required by the project.
- manage.py: Django management script for running various commands.
- Procfile: File specifying the commands to run on the server.

## Installation

There are two ways to run the ESIEEVERSE application:

### Option 1: Using a virtual environment (Recommended for speed but don't have acces to esieechat)

Create a virtual environment:
```
python3 -m venv esieeverse-env
```

Activate the virtual environment:
```
source esieeverse-env/bin/activate
```

Install the Python dependencies:
```
pip install -r requirements.txt
```

Start the application:
```
python manage.py runserver
```

Option 2: Using Docker

Build the Docker image:
```
docker build -t esieeverse .
```

Run the Docker container:
```
docker run -p 80:8000 esieeverse
```

The application will be accessible at http://localhost/

## Accessing the Application
You can access the ESIEEVERSE application by visiting https://esieeverse.up.railway.app/auth/login/. Please note that the server might be slow due to heavy traffic. For local development, use the local URL mentioned above.

We hope you enjoy using ESIEEVERSE and find it helpful in managing your student life at ESIEE Paris!