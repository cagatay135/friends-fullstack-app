from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Quote)

@admin.register(models.Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'portrayed_by')

