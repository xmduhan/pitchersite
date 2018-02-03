#!/usr/bin/env python
# encoding: utf-8

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(receivers, title, content, attachments=[]):
    '''
    parameters:
        receivers  list formation
        title
        content
        attachments  list of attachments file

    returns
        True if successed

    edit config file: ~/.send_mail_profile

        stmp_server=smtp.domian.com
        stmp_port=25
        stmp_user=username
        stmp_password=*********
        stmp_sender=username@domian.com
    '''
    try:
        home = os.path.expanduser('~')
        profile = os.path.join(home, '.send_mail_profile')
        config = dict(line.strip().split('=') for line in open(profile) if line.find('=') != -1)
        stmp_server = config['stmp_server']
        stmp_port = config['stmp_port']
        stmp_user = config['stmp_user']
        stmp_password = config['stmp_password']
        stmp_sender = config['stmp_sender']
    except Exception:
        print 'Can not read config file: ~/send_mail_profile'
        raise

    # Decode mail content
    message = MIMEMultipart()
    contentPart = MIMEText(content, 'html', 'utf-8')
    message.attach(contentPart)
    for filename in attachments:
        fn = os.path.split(filename)[-1]
        attMimeText = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
        attMimeText["Content-Type"] = u'application/octet-stream'
        attMimeText["Content-Disposition"] = 'attachment; filename="%s"' % fn
        message.attach(attMimeText)

    # Set mail header
    message['to'] = ','.join(receivers)
    message['from'] = stmp_sender
    message['subject'] = title

    # Send mail
    # smtp = smtplib.SMTP(stmp_server, stmp_port)
    smtp = smtplib.SMTP_SSL(stmp_server, stmp_port)
    smtp.login(stmp_user, stmp_password)
    smtp.sendmail(stmp_sender, receivers, message.as_string())
    smtp.quit()

    return True
