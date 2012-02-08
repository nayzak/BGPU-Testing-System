import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tornado.options import options
from whirlwind.core.log import Log


def sendmail(recipient_addr, recipient_name, subject, text, html=None):
    msg = MIMEMultipart()
    msg['From'] = '{} <{}>'.format(options.email_notification_name, options.email_notification_address)
    msg['Reply-To'] = '{} <{}>'.format(options.email_notification_name, options.email_notification_address)
    msg['Return-Path'] = options.email_notification_address
    msg['X-Mailer'] = 'The Bat! (v3.0.1.33) Professional'
    msg['To'] = '{} <{}>'.format(recipient_name, recipient_addr)
    msg['Subject'] = subject
    msg.attach(MIMEText(text, 'plain'))
    if html:
        msg.attach(MIMEText(html, 'html'))

    try:
        s = smtplib.SMTP(options.smtp_host, options.smtp_port)
        s.login(options.smtp_user, options.smtp_password)
        s.sendmail(options.email_notification_address, [recipient_addr], msg.as_string())
        Log.info('Sended email to ' + recipient_addr)
    except smtplib.SMTPException as e:
        Log.error(e.message)
