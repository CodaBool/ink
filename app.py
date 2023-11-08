import datetime
import pytz
import random
from bs4 import BeautifulSoup
from google.oauth2 import service_account
from googleapiclient.discovery import build

timezone = 'America/New_York'
pytz_timezone = pytz.timezone(timezone)
today = datetime.date.today()

# Replace with data
backgrounds = ['2.jpg', '6.jpg', '7.jpg', '8.jpg', '19.jpg', '20.jpg', '22.jpg', '23.jpg', '24.jpg', '26.jpg', '27.jpg', '1.png', '3.png', '4.png', '5.png', '9.png', '10.png', '11.png', '12.png', '13.png', '14.png',  '17.png', '18.png', '21.png', '25.png']
random_index = random.randint(0,len(backgrounds)-1)

# Load the HTML file
with open('./data/template.html', 'r') as file:
  filedata = file.read()

with open('./data/count.txt', 'r') as file:
  count = file.read()

with open('./data/release_count.txt', 'r') as file:
  r_count = file.read()

# Release
if int(count) == 0:
  print("release =", r_count)
  # Print days until release
  target_date_str = "2023-07-21"
  target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
  delta = target_date - today
  days_until = delta.days

  background = ''
  if int(r_count) == 0:
    background = 'dune.png'
    target_date_str = "2024-03-15"
  elif int(r_count) == 1:
    background = 'romulus.png'
    target_date_str = "2024-08-16"
  elif int(r_count) == 2:
    background = 'joker.png'
    target_date_str = "2024-10-04"
  elif int(r_count) == 3:
    background = 'prince.png'
    target_date_str = "2024-01-18"
  elif int(r_count) == 4:
    background = 'dark_forces.png'
    target_date_str = "2024-02-28"
  elif int(r_count) == 5:
    background = 'plane.jpg'
    target_date_str = "2024-10-31"

  with open('./data/release_count.txt', 'w') as file:
    if int(r_count) == 5:
      r_count = 0
    else:
      r_count = int(r_count) + 1
    file.write(str(r_count))

  target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d").date()
  delta = target_date - today
  days_until = delta.days
  print("background", background)
  print(days_until, "days")
  
  filedata = filedata.replace('REPLACE_IMG', background)
  filedata = filedata.replace('TEXT', str(days_until))

# Meeting
elif int(count) == 1:
  print('meeting')
  # Set the credentials
  creds = service_account.Credentials.from_service_account_file('key.json')
  # events = service.events().list(calendarId='primary', pageToken=page_token).execute()
  # Set the start and end times for the events query
  start_time = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
  end_time = (datetime.datetime.utcnow() + datetime.timedelta(days=7)).isoformat() + 'Z'

  # Build the service object for the Google Calendar API
  service = build('calendar', 'v3', credentials=creds)

  # Query the events for the next week
  events_result = service.events().list(calendarId='doug.moore@oddball.io', timeMin=start_time,
    timeMax=end_time, singleEvents=True, orderBy='startTime').execute()

  # Get the list of events from the result
  events = events_result.get('items', [])

  # Print the events
  meeting_count = 0
  first_event = ''
  for event in events:
    start_time = event['start'].get('dateTime', event['start'].get('date'))
    start_time = datetime.datetime.fromisoformat(start_time)
    # This could result in a bug where the first of the month does not show as an upcoming meeting
    if (today.day == start_time.day and today.month == start_time.month) or (today.day + 1 == start_time.day and today.month == start_time.month):
      meeting_count += 1
      now = datetime.datetime.now(pytz.timezone('America/New_York'))
      delta = start_time - now
      hours = delta.seconds // 3600
      minutes = (delta.seconds % 3600) // 60
      if first_event == '' and hours <= 3:
        print("hours, minutes", hours, minutes)
        if hours == 0:
          first_event = f'Meeting in {minutes} minutes'
        else:
          first_event = f'Meeting in {hours}h {minutes}m'
      if first_event == '' and hours > 3:
        print("hours", hours)
        first_event = f'Meeting in {hours}h'


  statement = ""
  if meeting_count > 0:
    statement = first_event
  else:
    statement = "No meetings"
  # TODO: make this more dynamic
  print("background", backgrounds[random_index])
  filedata = filedata.replace('font-size: 6em;', 'font-size: 3em;')
  filedata = filedata.replace('REPLACE_IMG', backgrounds[random_index])
  filedata = filedata.replace('TEXT', statement)

# Time
elif int(count) == 2:
  print('time')
  now = datetime.datetime.now(pytz.timezone('America/New_York'))
  hour = now.strftime("%-I")
  minute = now.strftime("%M")
  am_pm = now.strftime("%p").lower()
  print("{}:{} {}".format(hour, minute, am_pm))
  print("background", backgrounds[random_index])
  filedata = filedata.replace('REPLACE_IMG', backgrounds[random_index])
  filedata = filedata.replace('TEXT', "{}:{} {}".format(hour, minute, am_pm))

elif int(count) == 3:
  print('bun')
  filedata = filedata.replace('REPLACE_IMG', "cow.jpg")
  filedata = filedata.replace('TEXT', "I ❤️ Sierra")

with open('./data/count.txt', 'w') as file:
  if int(count) == 3:
    count = 0
  else:
    count = int(count) + 1
  file.write(str(count))

with open('./data/index.html', 'w') as file:
  file.write(filedata)
