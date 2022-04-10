from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from . import models


class GamesAdmin(admin.ModelAdmin):
    list_display=('name',)

admin.site.register(models.User, UserAdmin)
admin.site.register(models.Games, GamesAdmin)
admin.site.register(models.Genre)
# Register your models here.
