from django.contrib import admin

from .models import UserProfile, Question, Choice

admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Choice)
