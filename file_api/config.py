import os

# This file should be used only for containing environment variables, nothing else
APP_NAME = os.environ["APP_NAME"] = "file_api"
COMMIT = os.environ["COMMIT"] = "LOCALE"
LOG_LEVEL = os.environ["LOG_LEVEL"] = "DEBUG"
DRIVE_CLIENT_SECRETS_FILE = os.environ["CLIENT_SECRETS_FILE"] = "client_secret.json"
DRIVE_APP_SECRET_KEY = os.environ["DRIVE_APP_SECRET_KEY"] = ""
DRIVE_REDIRECT_URI = os.environ["DRIVE_REDIRECT_URI"] = "http://localhost:8080/oauth2callback"
os.environ["PYTHONUNBUFFERED"] = "yes"

# When running locally, disable OAuthlib's HTTPs verification.
# When running in production *do not* leave this option enabled.
# This is used for Google Drive
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
