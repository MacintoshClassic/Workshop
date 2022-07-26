from django.contrib import admin
from .models import *

admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Mechanic)
admin.site.register(OrderInitialDetails)
admin.site.register(OrderAdditionalDetails)
