from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

scopes = ['https://www.googleapis.com/auth/calendar.events']


#create flow object
flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
credentials = flow.run_console()

#pickle can save python objects in a file
import pickle
pickle.dump(credentials, open("token.pkl", "wb"))
credentials = pickle.load(open("token.pkl", "rb"))

#Create service object for calendar api
service = build("calendar", "v3", credentials=credentials)


# -------------------------------------------------------------
from datetime import datetime, timedelta
timezone = 'America/New_York' 
#CREATE AN EVENT: function modified from IndianPythonista.
import datefinder #FIRST: pip install datefinder
def create_event(start_time_str, summary, location, duration=1, description=None):
    matches = list(datefinder.find_dates(start_time_str))
    if len(matches):
        start_time = matches[0]
        end_time = start_time + timedelta(hours=duration)
    event = {
            'summary': summary,
            'location': location,
            'description': 'Fun with the Google Calendar API!',
            'start': {
                'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24*60},
                    {'method': 'popup', 'minutes':10},
                ],
            },
    }
    return service.events().insert(calendarId='primary', body=event).execute()
