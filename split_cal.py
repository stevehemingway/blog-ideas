#!/usr/bin/env python3
import re
import os
from icalendar import Calendar

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def extract_ics_data(ics_file):
    with open(ics_file, 'r') as file:
        cal = Calendar.from_ical(file.read())
    
    for component in cal.walk():
        if component.name == "VTODO":
            summary = component.get('summary')
            print(f"summary is {summary}")
            description = component.get('description', '')
            # start_date = component.get('dtstart').dt
            # end_date = component.get('dtend').dt
            # location = component.get('location', '')
            
            if summary:
                filename = sanitize_filename(summary) + '.txt'
                with open(filename, 'w', encoding='utf-8') as output_file:
                    output_file.write(f"Summary: {summary}\n")
                    output_file.write(f"Description: {description}\n")
                    # output_file.write(f"Start Date: {start_date}\n")
                    # output_file.write(f"End Date: {end_date}\n")
                    # output_file.write(f"Location: {location}\n")
                
                print(f"Created file: {filename}")

if __name__ == "__main__":
    ics_file = input("Enter the path to your ICS file: ")
    if os.path.exists(ics_file):
        extract_ics_data(ics_file)
    else:
        print("The specified file does not exist.")
