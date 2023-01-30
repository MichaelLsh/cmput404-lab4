from django.contrib import admin
# Let the admin interact with an app
# Register your models here.
# from django.contrib import admin

from .models import Choice, Question

admin.site.register(Choice)
admin.site.register(Question)