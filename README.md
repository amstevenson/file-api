# file-api

A micro-service that acts as the backend for authenticating a user via Google Drive API's. After authentication, the
user token will be sent back to file-frontend, which will allow for authenticated file uploads to be performed.

If you are going to make use of this project, you will need to follow the steps related to setting up a Google Drive Api
project (https://developers.google.com/drive/v3/web/quickstart/python). The secret file will need to be placed in the
main directory of this service.

After this file has been placed in the main directory, change the DRIVE_APP_SECRET_KEY environment variable in config.py
to reflect the value of your secret key found within the file you inserted. 

## Running

Can use a virtualenv, although there isn't much here for now. Quickest way is to use python ./manage.py runserver.

### Virtualenv

1) Virtualenv venv
2) source venv/Scripts/activate - for windows
or source venv/bin/activate - mac
3) install dependencies (can use requirements.txt for this)
4) set FLASK_APP variable with
    "set FLASK_APP=manage.py" (for windows)
    or "export FLASK_APP=manage.py" (for mac)
5) flask run