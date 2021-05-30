from django.contrib.admin import ModelAdmin


class CommentAdmin(ModelAdmin):

    @staticmethod
    def cleanup_text(modeladmin, request, queryset):
        pass

    @staticmethod
    def author__first_name(obj):
        return obj.author.first_name

    @staticmethod
    def author__username(obj):
        return obj.author.username

    @staticmethod
    def movie__title(obj):
        return obj.movie.title

    @staticmethod
    def comment_date(obj):
        return obj.created.strftime("%d.%m.%Y")

    ordering = ['author__username', 'movie__title']
    list_display = ['id', 'author__username', 'author__first_name', 'movie__title', 'comment_date']
    list_per_page = 50
    list_filter = ['author__username', 'movie__title']
    search_fields = ['author__username', 'movie__title']
    actions = ['cleanup_text']


class GenreAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name'],
                'description': 'Name of movies genre'
                }
         )
    ]
    ordering = ['id']
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_per_page = 20
    search_fields = ['name']


class MovieAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'created']}),
        ('External Information',
         {
             'fields': ['genre', 'released'],
             'description': (
                 'These fields are going to be filled with data parsed'
                 'from external databases.'
             )
         }
         ),
        (
            'User Information',
            {
                'fields': ['rating', 'description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['created']

    @staticmethod
    def released_year(obj):
        return obj.released.year

    @staticmethod
    def cleanup_description(modeladmin, request, queryset):
        queryset.update(description=None)

    ordering = ['id']
    list_display = ['id', 'title', 'genre', 'released_year']
    list_display_links = ['id', 'title']
    list_per_page = 20
    list_filter = ['genre']
    search_fields = ['title']
    actions = ['cleanup_description']
