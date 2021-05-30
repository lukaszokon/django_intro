from django.db.models import CharField, Model, ForeignKey, DateTimeField, DateField, \
    IntegerField, TextField, DO_NOTHING, CASCADE
from django.contrib.auth.models import User


# Create your models here.


class Genre(Model):
    name = CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(Model):
    title = CharField(max_length=128)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField(null=True)
    created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(Model):
    text = TextField()
    author = ForeignKey(User, on_delete=CASCADE)
    movie = ForeignKey(Movie, on_delete=CASCADE)
    created = DateTimeField(auto_now_add=True)