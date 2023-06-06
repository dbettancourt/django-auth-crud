from django.contrib import admin
from .models import Task

class TasAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )


# Register your models here.
admin.site.register(Task)