import requests
import icalendar
from requests import models

def get_events(url, event_summaries=None):
    '''
    Returns all events from the given calendar that match one of the provided event summaries.
    '''
    try:
        raw_data = requests.get(url)
    except models.MissingSchema as error:
        raise ValueError("Invalid url.")

    events = { 'events': [] }
    calendar = icalendar.Calendar.from_ical(raw_data.text)
    if event_summaries:
        event_summaries = list_to_lower(event_summaries)
        for event in calendar.walk('VEVENT'):
            if event.get('summary').lower() in event_summaries:
                events['events'].append( {'summary': event.get('summary'), 'date': str(event.decoded('dtstart'))} )
    else:
        for event in calendar.walk('VEVENT'):
            events['events'].append( {'summary': event.get('summary'), 'date': str(event.decoded('dtstart'))} )
    
    return events

def list_to_lower(ol : list) -> list:
    '''
    Converts all the strings within the list to lower case.
    '''
    nl = []
    for i in ol:
        try:
            nl.append(i.lower())
        except ValueError as error:
            raise ValueError('Invalid type: ' + error)
    return nl

if __name__ == '__main__':
    results = get_events('http://www.easttroy.k12.wi.us/pro/events_ical_subscribe.cfm?detailid=659489&categoryids=19&categoryids2=all&facultyflag=0')
    for result in results['events']:
        print(result)