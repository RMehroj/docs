from django.contrib import admin
from api.v1.task import models

@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'file',
        'group',
    ]

