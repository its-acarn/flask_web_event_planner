from app.models.event import *


event1 = Event("24-12-20", "Christmas Eve", 15, "Ballroom", "Party with disco")
event2 = Event("25-12-20", "Christmas Day", 25, "Dining Hall", "Meal and Carol Singing")
events = [event1, event2]


def add_new_event(event):
    events.append(event)
