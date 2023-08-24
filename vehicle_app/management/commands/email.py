from email.message import EmailMessage
from .app2 import password
import ssl
import smtplib
from vehicle_app.models import *
from datetime import datetime, timedelta
import django
from django.core.management.base import BaseCommand
# from vehicle_app.models import *

# from . .models import *
django.setup()
dr = Vehicle.objects.all()
lis = []
inspec = []


def test():
    date = datetime.now().date()
    for dre in dr:
        datew = dre.Insuarance_expiry_date
        difference = datew-date
        if difference.days > 30 and dre.Plate_no in lis:
            lis.remove(dre.Plate_no)
            return False
        if difference.days < 30 and dre.Plate_no not in lis:
            email_sender = 'shixlinsey@gmail.com'
            email_password = "subikfmymdmarwja"

            email_receiver = 'wanjikulinsey@gmail.com'

            subject = "INSUARANCE ALERT"
            body = "Vehicle with number plate "+dre.Plate_no + \
                " insuarance is less than 30 days to expiry date"

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
                lis.append(dre.Plate_no)

    datew = dre.next_inspection_date
    difference = datew-date
    if difference.days > 30 and dre.Plate_no in inspec:
        inspec.remove(dre.Plate_no)
        return False
    if difference.days < 30 and dre.Plate_no not in inspec:
        email_sender = 'shixlinsey@gmail.com'
        email_password = "subikfmymdmarwja"

        email_receiver = 'wanjikulinsey@gmail.com'

        subject = "INSPECTION ALERT"
        body = "Vehicle with number plate "+dre.Plate_no + \
            " next inspection date is less than 30 days"

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
            inspec.append(dre.Plate_no)


class Command(BaseCommand):
    help = "Checking vehicle status"

    def handle(self, *args, **options):
        while True:
            test()
            time.sleep(2)
