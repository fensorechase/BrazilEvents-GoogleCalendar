# BrazilEvents-GoogleCalendar
Python script to write events to your Google Calendar using GCal API. Takes input event URL, then parses with BeautifulSoup.


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install BrazilEvents.

```bash
pip install BrazilEvents
```

## Usage
 First in GoogleAPI create a new project, and generate credentials. While generating credentials, be sure to create OAuth2.0 client ID, and store it in client_secret.json file in the same directory as this project. Here, we ensure a user gives consent before giving access to their Google Calendar to read/write.

```python
import BrazilEvents
eventScraper.py

Please visit this URL to authorize this application: [paste this URL into a web browser]
Enter the authorization code: [enter your authorization code]
Enter full event URL (n to quit): http://www.calendariodoagronegocio.com.br/Evento/visualizar/portugues/3226
Enter full event URL (n to quit): n

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

