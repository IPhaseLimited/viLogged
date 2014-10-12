from viLogged import settings
from django.core.mail import send_mail
import urllib
import urllib2
import base64
import barcode
from barcode.writer import ImageWriter


class Utility():

    @staticmethod
    def send_email(mail_title, message, recipients):
        email = settings.EMAIL_HOST_USER
        return send_mail(mail_title, message, email, recipients, fail_silently=False)

    @staticmethod
    def sms(sms_api=None, params=None):
        if params is None:
            params = {"username":"musakunte@gmail.com","password": "1979mall", "sender": "Musa",
                      "mobiles": "2348093976395", "message": "test sms"}
        if sms_api is None:
            sms_api = "http://login.betasms.com/customer/api/"

        data = urllib.urlencode(params)
        req = urllib2.Request(sms_api, data)
        return urllib2.urlopen(req)

    @staticmethod
    def load_image_bin(filename):
        with open(filename, "rb") as imageFile:
            new_name = base64.b64encode(imageFile.read())
        return new_name

    @staticmethod
    def create_barcode(data):

        ean = barcode.get('code39', data, writer=ImageWriter())
        filename = ean.save(settings.MEDIA_ROOT+'/img/code39', options=dict(quiet_zone=0, text_distance=0, font_size=0))
        str_label = Utility.load_image_bin(filename)
        return str_label

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