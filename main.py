#install required python libraries
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
from google.colab import auth
from googleapiclient.discovery import build
import json

# Authenticate with Google (popup will appear)
auth.authenticate_user()
print(auth)