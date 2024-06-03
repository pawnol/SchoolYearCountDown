import requests
import icalendar
from requests import models

def get_events(url):
    '''
    Returns the events for a given calendar.
    '''
    try:
        raw_data = requests.get(url)
    except models.MissingSchema as error:
        raise ValueError("Invalid url.")

    dates = { 'events': [] }
    calendar = icalendar.Calendar.from_ical(raw_data.text)
    for event in calendar.walk('VEVENT'):
        if 'last' in event.get('summary').lower():
            dates['events'].append( {'type': 'last day', 'date': str(event.decoded('dtstart'))} )
    
    return dates

if __name__ == '__main__':
    print(get_events('http://www.easttroy.k12.wi.us/pro/events_ical_subscribe.cfm?detailid=659489&categoryids=19&categoryids2=all&facultyflag=0'))