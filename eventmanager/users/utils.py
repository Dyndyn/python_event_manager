import os
import secrets

from PIL import Image
from flask import url_for, current_app
from flask_mail import Message

from eventmanager import mail


def save_picture(form_picture):
    hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    name = hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', name)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return name


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='noreply@demo.com', recipients=[user.email])
    msg.html = '''
    <!DOCTYPE html>
    <head>
        <title>Password reset</title>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    </head>
    <body>
        <p >
            Dear {username}
        </p>
        <p>
            For your account a password reset was requested, please click on the URL below to reset it:
        </p>
        <p>
            <a href="{url}">Login link</a>
        </p>
        <p>
            <span >Regards </span>
        </p>
    </body>
    </html>
    '''.format(username=user.username, url=url_for('users.reset_token', token=token, _external=True))
    mail.send(msg)
