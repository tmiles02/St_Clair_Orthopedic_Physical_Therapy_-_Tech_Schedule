from google.colab import auth
auth.authenticate_user()

import gspread
from oauth2client.client import GoogleCredentials
gc = gspread.authorize(GoogleCredentials.get_application_default())

sh = gc.open('Tech Schedule Upload Form').sheet1

# Code to handle form submission and upload PDF calendar