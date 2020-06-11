from django.contrib import admin
from apps.web_personal.web_personal.models import User, Projects, Skills

# Register your models here.
admin.site.register(User)
admin.site.register(Projects)
admin.site.register(Skills)
