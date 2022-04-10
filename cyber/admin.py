from django.contrib import admin
from . import models

class GamesAdmin(admin.ModelAdmin):
    list_display=('name',)


admin.site.register(models.Games, GamesAdmin)
# Register your models here.
