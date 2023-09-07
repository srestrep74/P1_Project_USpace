from django.contrib import admin
from .models import *


admin.site.register(Reminder)
admin.site.register(Comment)
admin.site.register(Rating)