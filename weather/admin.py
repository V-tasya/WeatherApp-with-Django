from django.contrib import admin
from .models import City

'''admin is an integrated panel which allows developers and admins 
to manage app's data throw user-friendly web-interface
with admin we can create, change, delete and view recordings in databases
 connected with models. Every registered model will be displayed in the administrative panel
'''

# model registration for her appearance in admin
admin.site.register(City)
