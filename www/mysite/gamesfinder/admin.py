from django.contrib import admin

from .models import Game

from .models import Genre

admin.site.register(Game)

admin.site.register(Genre)
