from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required

from eventmanager import db
from eventmanager.events.forms import (EventForm)
from eventmanager.models import Event

events = Blueprint('events', __name__)


@events.route("/event/new", methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    if form.validate_on_submit():
        event = Event(title=form.title.data, description=form.description.data, date=form.date.data,
                      time=form.time.data, user=current_user)
        db.session.add(event)
        db.session.commit()
        flash('Your event has been created', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_event.html', title='New Post', form=form, legend='New Event')


@events.route("/event/<event_id>")
@login_required
def event(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template('event.html', title=event.title, event=event)


@events.route("/event/<event_id>/update", methods=['GET', 'POST'])
@login_required
def update_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.user != current_user:
        abort(403)
    form = EventForm()
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.date = form.date.data
        event.time = form.time.data
        db.session.commit()
        flash('Your event has been updated', 'success')
        return redirect(url_for('events.event', event_id=event.id))
    elif request.method == 'GET':
        form.title.data = event.title
        form.description.data = event.description
        form.date.data = event.date
        form.time.data = event.time
    return render_template('create_event.html', title='Update Post', form=form, legend='Update Event')


@events.route("/event/<event_id>/delete", methods=['POST'])
@login_required
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    if event.user != current_user:
        abort(403)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('main.home'))
