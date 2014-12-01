from viLogged import settings
from django.core.mail import send_mail
import urllib
import urllib2
import base64

import json


class Utility():

    @staticmethod
    def error_to_json(error):
        error_dict = {}
        for k in error:
            error_dict[k] = error[k]

        return json.dumps(error_dict)

    @staticmethod
    def send_email(mail_title, message, recipients):
        email = ''
        return send_mail(mail_title, message, email, recipients, fail_silently=False)

    @staticmethod
    def sms(sms_api=None, params=None):

        data = urllib.urlencode(params)
        req = urllib2.Request(sms_api, data)
        return urllib2.urlopen(req)

    @staticmethod
    def load_image_bin(filename):
        with open(filename, "rb") as imageFile:
            new_name = base64.b64encode(imageFile.read())
        return new_name


    @staticmethod
    def addevent(event_date, subject):
        try:
            import win32com.client
            oOutlook = win32com.client.Dispatch("Outlook.Application")
            appointment = oOutlook.CreateItem(1) # 1=outlook appointment item
            appointment.Start = event_date
            appointment.Subject = subject
            appointment.Duration = 20
            appointment.Location = 'Appointments'
            appointment.ReminderSet = True
            appointment.ReminderMinutesBeforeStart = 1
            appointment.Save()
            return True
        except ImportError:
            return False