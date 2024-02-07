from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name



class Game(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    rating = models.DecimalField(default=0, decimal_places=1, max_digits=2)
    nrated = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(blank=True, null = True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.text

