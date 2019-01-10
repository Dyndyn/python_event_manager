from datetime import datetime, timedelta, date

from flask_mail import Message
from sqlalchemy import and_

from eventmanager import mail, db
from eventmanager.models import Event


def send_notification():
    begin_time = datetime.now().time()
    end_time = (datetime.now() + timedelta(hours=1)).time()
    events = db.session.query(Event).filter(and_(Event.date == date.today(), Event.time >= begin_time, Event.time <= end_time)).all()
    print(events)
    for event in events:
        send_reset_email(event)


def is_date_within(check_time, hours=1):
    begin_time = datetime.now()
    end_time = datetime.now() + timedelta(hours=hours)
    return begin_time <= check_time <= end_time


def send_reset_email(event):
    with db.app.app_context():
        msg = Message('Notification', sender='noreply@demo.com', recipients=[event.user.email])
        msg.html = '''
        <!DOCTYPE html>
        <head>
            <title>Notification</title>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
        </head>
        <body>
            <p>
                Dear {username}
            </p>
            <p>
                The following event will happen within one hour:
            </p>
            <div class="media-body">
                <h2 class="article-title">{title}</h2>
                <div class="article-metadata">
                    <small class="text-muted">{date} {time}</small>
                </div>
                <p class="article-content">{description}</p>
            </div>
        </body>
        </html>
        '''.format(username=event.user.username, date=event.date, time=event.time, title=event.title,
                   description=event.description)
        mail.send(msg)
