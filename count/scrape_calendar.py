import requests
import icalendar

raw_data = requests.get("http://www.easttroy.k12.wi.us/pro/events_ical_subscribe.cfm?detailid=659489&categoryids=19&categoryids2=all&facultyflag=0")

calendar = icalendar.Calendar.from_ical(raw_data.text)
for event in calendar.walk('VEVENT'):
    print(event.get('SUMMARY'), event.get('DTSTART'), sep=', ')