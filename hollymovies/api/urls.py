from rest_framework import routers
from .views import MovieViewset, GenreViewset

router = routers.DefaultRouter()
router.register(r'movies', MovieViewset)
router.register(r'genres', GenreViewset)
