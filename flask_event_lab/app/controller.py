from app import app
from app.models.event_list import events, add_new_event
from app.models.event import *
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template('index.html', title='Home', events=events)

@app.route('/add_event', methods=['POST'])
def add_event():
    eventName = request.form['eventname']
    eventDate = request.form['eventdate']
    eventGuests = request.form['guestnumber']
    eventLocation = request.form['roomlocation']
    eventDescription = request.form['description']
    newEvent = Event(name = eventName, date = eventDate, num_of_guests = eventGuests, room_location = eventLocation, description = eventDescription)
    add_new_event(newEvent)

    return redirect('/')

    