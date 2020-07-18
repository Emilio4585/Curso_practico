from django.contrib import admin
from apps.web_personal.web_personal.models import User, Projects, Skills


# Register your models here.
class ProjectsInline(admin.StackedInline):
    model = Projects


class SkillsInline(admin.StackedInline):
    model = Skills


class UserAdmin(admin.ModelAdmin):
    inlines = [ProjectsInline, SkillsInline, ]


admin.site.register(User, UserAdmin)
