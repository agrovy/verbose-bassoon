from django.shortcuts import render, redirect
from .models import Genre, Game, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def homepage(request):        
    context = {"games" : Game.objects.all().order_by('-rating')}
    return render(request, 'gamesfinder/homepage.html', context)

@login_required(login_url='/login')
def gamepage(request, game_id):
    context = {"game" : Game.objects.get(id=game_id)}
    return render(request,'gamesfinder/gamepage.html', context)

@login_required(login_url='/login')
def post_review(request, game_id):
    text = request.POST['reviewtext']
    print(text, game_id)
    review = Review(text=text, game=Game.objects.get(id=game_id))
    review.save()
    return redirect (request.META['HTTP_REFERER'])

@login_required(login_url='/login')
def rate_game(request, game_id):
    rating = request.POST['rating']
    print(rating)
    game = Game.objects.get(id=game_id)
    if int(game.rating) == 0:
       game.rating = rating
       game.nrated = 1
    else:
      
        total = float(game.rating) * int(game.nrated) + int(rating)
        print(game.rating, game.nrated, total)
        game.nrated += 1
        game.rating = total/game.nrated
    

    game.save()
    return redirect(request.META['HTTP_REFERER'])
   
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)
        user = User.objects.create_user(username=username, password=password)
        
        if user:
            login(request, user)
            return redirect('gamesfinder:homepage')
        else:
            print('User already exists')
            return render(request, 'gamesfinder/login.html')    

    else:
        return render(request, 'gamesfinder/login.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('user authenticated')
            login(request, user)
            return redirect('gamesfinder:homepage')
        else:
            return render(request, 'gamesfinder/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'gamesfinder/login.html')
        
def signout(request):
    logout(request)
    return redirect('gamesfinder:homepage')

def genres(request):
    context = {"genres" : Genre.objects.all()}
    return render(request,'gamesfinder/genrepage.html', context)

def genre(request, genre_id):
    context = {"genre" : Genre.objects.get(id=genre_id),"game" : Game.objects.get}
   
    return render(request,'gamesfinder/genre.html', context)