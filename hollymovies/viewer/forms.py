import re
from datetime import date
from django.core.exceptions import ValidationError
from django.forms import CharField, DateField, ModelForm, IntegerField, ModelChoiceField, Textarea
from .models import Genre, Movie, Comment


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Wartość musi być z wielkiej litery.')


def exists_genre_validator(value):
    if Genre.objects.filter(name=value).exists():
        raise ValidationError('Podany gatunek już istnieje')


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Czasy przyszłe są nieprawidłowe.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class GenreForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Genre
        fields = '__all__'

    name = CharField(max_length=128, validators=[capitalized_validator, exists_genre_validator])


class CommentForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ['text']


class MovieForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Movie
        fields = '__all__'

    title = CharField(max_length=128, validators=[capitalized_validator])
    genre = ModelChoiceField(Genre.objects.order_by('name'))
    rating = IntegerField(min_value=1, max_value=10)
    released = PastMonthField()

    def clean_description(self):
        inital = self.cleaned_data['description']
        sentences = re.sub(r'\s*\. \s*', '.', inital).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == 'Komedia' and result['raitng'] > 5:
            self.add_error('genre' '')
            self.add_error('rating' '')
            raise ValidationError('Komedie nie są tak dobre, by były oceniane na więcej niż 5')
        return result
