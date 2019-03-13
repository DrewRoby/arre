from django.contrib import admin
from .models import Realtor
from .models import Listing

admin.site.register(Listing)
admin.site.register(Realtor)
