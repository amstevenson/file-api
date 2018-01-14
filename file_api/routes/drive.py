from flask import Blueprint, redirect, session, url_for, request, jsonify
from file_api.utils.driveutils import credentials_to_dict
import os
import logging
import google_auth_oauthlib.flow
import google.oauth2.credentials
import googleapiclient.discovery
import json

drive = Blueprint('drive', __name__)

SCOPES = ['https://www.googleapis.com/auth/drive']

# The client secret file is downloaded from the created project from the drive apis
DRIVE_CLIENT_SECRETS_FILE = os.getenv("CLIENT_SECRETS_FILE")
DRIVE_APP_SECRET_KEY = os.getenv("DRIVE_APP_SECRET_KEY")
DRIVE_REDIRECT_URI = os.getenv("DRIVE_REDIRECT_URI")
API_SERVICE_NAME = 'drive'
API_VERSION = 'v2'

logger = logging.getLogger()


@drive.route("/drive-request")
def drive_request():
    if 'credentials' not in session:
        # If credentials are not set
        return {"status": "200", "authorisation_url": get_authorisation_url()}

    # Load credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **session['credentials'])

    drive = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)

    files = drive.files().list().execute()

    # Save credentials back to session in case access token was refreshed.
    # TODO: In a production app, id likely want to save these
    #              credentials in a persistent database instead.
    session['credentials'] = credentials_to_dict(credentials)

    return jsonify(**files)


@drive.route('/get-authorisation-url', methods=["GET"])
def get_authorisation_url():
    # Create flow instance to manage the OAuth 2.0 Authorization Grant Flow steps.
    logger.info("Received request to authorise user")
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        DRIVE_CLIENT_SECRETS_FILE, scopes=SCOPES)

    flow.redirect_uri = DRIVE_REDIRECT_URI

    authorization_url, state = flow.authorization_url(
        # Enable offline access so that you can refresh an access token without
        # re-prompting the user for permission. Recommended for web server apps.
        access_type='offline',
        # Enable incremental authorization. Recommended as a best practice.
        include_granted_scopes='true')

    # Store the state so the callback can verify the auth server response.
    return json.dumps({"status": "200", "url": authorization_url, "state": state})


@drive.route('/get-credentials/<state>/<url>', methods=["GET"])
def get_credentials(state, url):
    # Specify the state when creating the flow in the callback so that it can
    # verified in the authorization server response.
    logger.info("Received request to retrieve user credentials")
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        DRIVE_CLIENT_SECRETS_FILE, scopes=SCOPES, state=state)

    flow.redirect_uri = DRIVE_REDIRECT_URI

    # Use the authorization server's response to fetch the OAuth 2.0 tokens.
    authorization_response = url
    flow.fetch_token(authorization_response=authorization_response)

    # Store credentials in the session.
    # TODO: In a production version, id likely want to save these
    #              credentials in a persistent database instead.
    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)

    # TODO: encrypt response credentials
    return json.dumps({"status": "200", "credentials": credentials_to_dict(credentials)})
