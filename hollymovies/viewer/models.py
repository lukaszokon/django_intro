from django.db.models import CharField, Model

# Create your models here.


class Genre(Model):
    name = CharField(max_length=128)
