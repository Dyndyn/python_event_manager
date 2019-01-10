import os

class Config:
    SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'dyndynroman@gmail.com'  # os.environ.get('EMAIL_USER')
    MAIL_PASSWORD =  # os.environ.get('EMAIL_PASS')

    JOBS = [
        {
            'id': 'job1',
            'func': 'eventmanager.event_notifications:send_notification',
            'trigger': 'cron',
            # 'year': 2017,
            # 'month': 3,
            # 'day': 22,
            # 'minute': 19,
            'second': 7
        }
    ]
