import datetime
from vehicle_app.models import *

# from models import *
# import smtplib
date = datetime.datetime.now()

print(date)
dr = Vehicle.objects.get(Plate_no='KDC 576B')
print(dr)
