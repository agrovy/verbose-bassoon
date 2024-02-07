from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "gamesfinder"

urlpatterns = [
    path('', views.homepage, name = "homepage"),
    path('gamepage/<int:game_id>', views.gamepage, name = 'gamepage'),
    path('review/<int:game_id>', views.post_review, name = 'review'),
    path('rate/<int:game_id>',views.rate_game, name = 'rate'),
    path('login',views.signin, name = 'login'),
    path('register',views.register,name = 'register'),
    path('logout',views.signout,name = 'logout'),
    path('genres',views.genres,name = "genres"),
    path('genre/<int:genre_id>',views.genre,name = "genre"),
]




    


